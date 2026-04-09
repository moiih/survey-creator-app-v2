from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db import connection
from poll.forms import PollForm, UserSignUpForm
from poll.models import PollModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_signup(request):
    if not request.user.is_authenticated:        
        if request.method == 'POST':
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                # messages.success(request, 'Account Created Successfully!!')
                return redirect('login')
        else:
            form = UserSignUpForm()

        context = { 'form': form, 'user': request.user }   
        return render(request, 'poll/signup.html', context)
    
    else:
        return redirect('/home/')



def user_login_index(request):
    if not request.user.is_authenticated:        
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)                
                if user is not None:
                    login(request, user)
                    # print('\n\nUser id :', request.user.id, end='\n\n\n')
                    return redirect('/home/')
        else:
            form = AuthenticationForm()   

        context = { 'form': form, 'user': request.user }   
        return render(request, 'poll/login.html', context)

    else:
        return redirect('/home/')



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')




#   Below Two View Methods are for "All Poll of all Users".


def home(request):
    if request.user.is_authenticated:
            
        poll = PollModel.objects.all()    

        # poll = PollModel.objects.all()    

        # if request.method == 'POST':
        #     if str(request.POST.get('psearch')) == 'Mohit':
        #         print('\n\nState =', request.POST.get('psearch'), end = '\n\n')
        #     else:
        #         print('\n\nState = Shoot', end = '\n\n')

        context = { 'poll': poll, 'user': request.user, 'req_id': str(request.user.id) }   
        return render(request, 'poll/home.html', context)
    
    else:
        return redirect('login')   



def delete(request, poll_id):    
    if request.user.is_authenticated:

        poll = PollModel.objects.get(pk=poll_id)
        poll.delete()

        return redirect('home')

    else:
        return redirect('login')



#   Rest Below View Methods are "Current - User Specific".

def my_home(request):
    if request.user.is_authenticated:
        
        request_id = str(request.user.id)
        poll = PollModel.objects.all().filter(user_id__exact=request_id)


        context = { 'poll': poll, 'user': request.user }   
        return render(request, 'poll/my_home.html', context)
    
    else:
        return redirect('login')    
  


def create_poll(request):
    if request.user.is_authenticated:

        if request.method == 'POST':                 

            form = PollForm(request.POST)
            if form.is_valid():              
                # if request.POST.get('state_option_four'):
                #     checkbox_option_form = PollModel()
                #     checkbox_option_form.state_option_four = request.POST.get('state_option_four')
                #     checkbox_option_form.save()            
                form.save()
                messages.success(request, 'Your Poll Is Ready!')      


                cur = connection.cursor()
                cur.execute('select max(poll_id) from poll_table_temp')

                #    Extracting the latest "poll_id" from table.
                last_poll_id = cur.fetchall()
                last_poll_id = list(last_poll_id[0])[0]
                print('\n\n Last Poll ID :', last_poll_id, end='\n\n\n')

                #    Assinging the value of "user_id" from table.
                query = 'update poll_table_temp set user_id = ' + str(request.user.id) + ' where poll_id = ' + str(last_poll_id)
                cur.execute(query)
                connection.commit()
                print('\n\n Query :', query, end='\n\n\n')

                
        else:
            form = PollForm()

        context = { 'form': form, 'user': request.user }   
        return render(request, 'poll/createpoll.html', context)
    
    else:
        return redirect('login')    
    



def cast_vote(request, poll_id):
    if request.user.is_authenticated:

        poll = PollModel.objects.get(pk=poll_id)  ## It needs to be outside the "if" statement below. Otherwise, it will through [Error: 'poll' is refernced before assignment.]
                                                  ## This is becz the "Object of Model" should be declared outside any block (like: if request.method == ...., etc) inside the funtion.

        if request.method == 'POST':
            selected_option = request.POST['poll']   ## No "Round-Brackets" directly after "POST" (like here in 'request.POST[''])
            if selected_option == 'option1':
                poll.option_one_count += 1
            elif selected_option == 'option2':
                poll.option_two_count += 1
            elif selected_option == 'option3':
                poll.option_three_count += 1
            elif selected_option == 'option4':
                poll.option_four_nota_count += 1
            else:
                return HttpResponse('<h1><center>Invalid Form</center></h1>')
            
            poll.save()
            return redirect('result', poll_id)

        context = { 'poll': poll, 'user': request.user }
        return render(request, 'poll/vote_poll.html', context)

    else:
        return redirect('login')   
    


def result(request, poll_id):
    if request.user.is_authenticated:
        poll = PollModel.objects.get(pk=poll_id)

        context = { 'poll': poll, 'user': request.user }
        return render(request, 'poll/result.html', context)        
    else:
        return redirect('login')    
    


def my_delete(request, poll_id):
    if request.user.is_authenticated:

        poll = PollModel.objects.get(pk=poll_id)
        poll.delete()

        return redirect('myhome')

    else:
        return redirect('login')    
    



def edit(request, poll_id):
    if request.user.is_authenticated:

        if request.method == 'POST':

            poll = PollModel.objects.get(pk=poll_id)
            form = PollForm(request.POST, instance = poll)

            if form.is_valid():
                if request.POST.get('chkbox') != None:  ## This ['chkbox'] is just a normal variable here that we have passed as the "reference" in 
                                                        ##   the "edit1.html" file in the [name="chkbox" in 'checkbox' form input].
                    poll.option_one_count = 0           ## This is done to check the "condition" whether the User want to 'Continue As New Form' or not.
                    poll.option_two_count = 0           ## If the User checks the CheckBox then the value of the ["chkbox"] will become ('1'),
                    poll.option_three_count = 0         ##   else [None (KeyWord)] will be passed. So, we can check it in view.                           
                    poll.option_four_nota_count = 0  ###            
                                                                    
                form.save()
                messages.success(request, 'Your Poll Is Updated!')
        else:
            poll = PollModel.objects.get(pk=poll_id)
            form = PollForm(instance = poll)

        context = { 'poll': poll, 'form': form, 'user': request.user }
        return render(request, 'poll/edit_poll.html', context)

    else:
        return redirect('login')    
    
    


to_ttags = ''

def search(request):
    if request.user.is_authenticated:

        if request.method == 'GET':

            global to_ttags
            to_ttags = request.GET.get('psearch')        

            search = request.GET.get('psearch')        
            # print('\n\n\tString :', search, end='\n\n')
            poll = PollModel.objects.all().filter(question__icontains=search) ## "__icontains" is called the "Lookup" which filter the results by removing Case-Sensitivity.
            
        context = { 'poll': poll, 'search': search, 'req_id': str(request.user.id) }
        return render(request, 'poll/search_poll.html', context)   

    else:
        return redirect('login')    



def pass_to_ttags():
    global to_ttags
    return to_ttags
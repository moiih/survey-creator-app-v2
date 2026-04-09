from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import QuizModel
from django.db.models import Q

# Create your views here.


            #### Copy Unsuccessfull in JS (Work Under Construction...)

def quiz_home(request): 
    if request.user.is_authenticated:   
        # context = { 'chk_user': request.user.is_authenticated }
        return render(request, 'quiz/quiz_home.html')
    else:
        return redirect('login')


def set_quiz_title(request):

    # if 'quiz_title' in request.session:
    #     del request.session['quiz_title']

    if request.user.is_authenticated:   
        if request.method == 'POST':
            print('\nQuiz Title :', request.POST.get('quiz_title'), end='\n\n') 
            request.session['quiz_title'] = str(request.POST.get('quiz_title'))
            request.session['page_count'] = 1
            return redirect('create_quiz')         
        return render(request, 'quiz/set_quiz_title.html')
    else:
        return redirect('login')



def create_quiz(request):    

    # print('\nQuiz Title :', request.session['quiz_title'], end='\n\n')      
    
    if request.user.is_authenticated:   
            
        qtitle = ''
        total_questions = ''
        if request.method == 'POST' or request.method == 'FILES':                        
                                    
            print('\nQuestion :', request.POST.get('question'), end='\n\n')

            # title = request.POST.get('quiz_title')
            # question = request.POST.get('question')
            # image = request.FILES['image']            

            # upload_to_model = QuizModel(user_id=request.user.id, quiz_title=title, question=question, image=image)
            # upload_to_model.save()

            # image = request.FILES['image']

            # correct_option = 'correct_option_' + str(request.session['page_count'])
            # print('\nCorrect Option :', correct_option, end='\n\n')      

            quiz = QuizModel()

            quiz.quiz_title = request.POST.get('quiz_title')
            quiz.poller = request.POST.get('quiz_title')
            quiz.question = request.POST.get('question')            
            quiz.image = request.FILES.get('image')  ## To make ("ImageField / FileField") 'Optional' then add [ blank=True, null=True ] in "models.py" and use ["request.FILES.get('image_field_name')"] while manually catching and saving the value of "image_field_name" from HTML Form in "views.py".
            quiz.user = request.user
            # quiz.correct_option = request.POST.get('correct_answer')

            print('\nCorrect Answer :', request.POST.get('correct_answer_text'), end='\n\n')
            if request.POST.get('correct_answer_text'):
                quiz.correct_option = request.POST.get('correct_answer_text')
            else:    
                if request.POST.get('correct_answer') == 0 or request.POST.get('correct_answer') == '0':
                    quiz.correct_option = 'NULL'
                else:
                    quiz.correct_option = request.POST.get('correct_answer')


            # if request.session['page_count'] == 1:
            #     quiz.correct_option_1 = request.POST.get('correct_answer')
            # elif request.session['page_count'] == 2:
            #     quiz.correct_option_2 = request.POST.get('correct_answer')
            # elif request.session['page_count'] == 3:
            #     quiz.correct_option_3 = request.POST.get('correct_answer')
            # elif request.session['page_count'] == 4:
            #     quiz.correct_option_4 = request.POST.get('correct_answer')
            # elif request.session['page_count'] == 5:
            #     quiz.correct_option_5 = request.POST.get('correct_answer')
            # elif request.session['page_count'] == 6:
            #     quiz.correct_option_6 = request.POST.get('correct_answer')
            


            if request.POST.get('option_one'):
                quiz.option_one = request.POST.get('option_one')      
            if request.POST.get('option_two'):
                quiz.option_two = request.POST.get('option_two')      
            if request.POST.get('option_three'):
                quiz.option_three = request.POST.get('option_three')      
            if request.POST.get('option_four'):
                quiz.option_four = request.POST.get('option_four')      
            if request.POST.get('option_five'):
                quiz.option_five = request.POST.get('option_five')      
            if request.POST.get('option_six'):
                quiz.option_six = request.POST.get('option_six')      
            
            quiz.save()  ## Committing Inserted Data

            if request.POST.get('session_state') == '1': 
                request.session['page_count'] = request.session['page_count'] + 1
                return redirect('create_quiz')
            else:
                qtitle = request.session['quiz_title']                            
                total_questions = request.session['page_count']

                if 'quiz_title' in request.session:
                    del request.session['quiz_title']                            

                if 'page_count' in request.session:
                    del request.session['page_count']
                messages.success(request, 'Your Survey Created Succesfully!!')

            return redirect('/quiz/get_titles/')
            
        context = { 'qtitle': qtitle, 'total_questions': total_questions }
        return render(request, 'quiz/create_quiz.html', context)

    else:
        return redirect('login')





def get_titles(request):
    if request.user.is_authenticated: 

        print('\n\nCurrent Username :', request.user, end='\n\n')

        request_id = str(request.user.id)          
        titles_quiz = QuizModel.objects.filter(user_id__exact=request_id).exclude(quiz_title=None).values('quiz_title').distinct()  ## This will fetch all distinct values of "quiz_title" [ values('quiz_title).distinct() ]  where the "user_id" is the equal to the "Current User ID"(request.user.id).
        print('\n\nGet Titles Object :', titles_quiz, end='\n\n')
        # print('\n\nUser Email', request.user.email, end='\n\n')

        context = { 'titles_quiz': titles_quiz }
        return render(request, 'quiz/show_titles.html', context)

    else:
        return redirect('login')

        



def show_quiz(request, quiz_title):

    ## Utility "function" to extract all "digits" from a string.
    def extract_digits(string_value):   
            collect_digits = []
            for s in string_value:
                print('\n\nFor Loop Object :', s)
                s = str(s)            
                # print('Loop Object (str) :', s, end='\n\n')            
                # print('Loop Object (str type) :', type(s), end='\n\n')
                temp = ''
                for ch in s:   
                    if ch.isdigit():
                        temp = temp + ch
                collect_digits.append(temp)
            
            return collect_digits

    ######## ######### ######### ######### ######## ######### ########

    poller_flag = 0

    if request.user.is_authenticated: 


        ### This "if-else" is serving as a "decorator part of the function" for "Sharing/Copying Survey Link" to Other Users.
        if 'pAcfizz' in quiz_title:
            poller_flag = 1
            temp_title = quiz_title.split('pAcfizz')
            print('\nTemp Title [split] :', temp_title, end='\n\n')

            request_id = temp_title[1]
            print('\nRequest ID [pAcfizz] :', request_id, end='\n\n')
            quiz_title = temp_title[2]
            print('\nQuiz Title [pAcfizz] :', quiz_title, end='\n\n')
        else:
            request_id = request.user.id


        
        print('\nQuiz Title :', quiz_title)
        print('\nUser Email :', request.user.email, end='\n\n')
        if QuizModel.objects.filter(quiz_title=quiz_title, poller=request.user).exists():                    
        # if QuizModel.objects.filter(quiz_title=quiz_title, poller=request.user.email).exists():
            messages.info(request, "You've already attempted that survey !!")
            return redirect('')
        else:
            if not QuizModel.objects.filter(quiz_title=quiz_title, poller=request.user.email).exists():

                # if quiz_title[0:10] == 'pAcfizz':  ## Url seperation keyword : 'pAcfizz'
                # if 'pAcfizz' in quiz_title:                      ### This "if-else" is serving as a "decorator part of the function" for "Sharing/Copying Survey Link" to Other Users.
                #     poller_flag = 1
                #     temp_title = quiz_title.split('pAcfizz')
                #     print('\nTemp Title [split] :', temp_title, end='\n\n')

                #     request_id = temp_title[1]
                #     print('\nRequest ID [pAcfizz] :', request_id, end='\n\n')
                #     quiz_title = temp_title[2]
                #     print('\nQuiz Title [pAcfizz] :', quiz_title, end='\n\n')
                # else:
                #     request_id = request.user.id
                
                show_quiz = QuizModel.objects.filter(poller__exact=quiz_title, user_id__exact=request_id)                
                print('\n\nShow Quiz Object :', show_quiz, end='\n\n')        
                
                collect_id = extract_digits(show_quiz)   ## This will store all the required id(s) as all options are passed as their (id) names in the Template.                
                

                print('\n\nCollect ID(s) [Extraxted] :', collect_id, end='\n\n')
                
                count_questions = []
                for i in range(1, len(collect_id)):
                    count_questions.append(i)

                if request.method == 'POST':    

                    pseudo_response = QuizModel.objects.filter(poller__exact=quiz_title)
                    print('\nPseudo Response :', pseudo_response, end='\n\n')
                    print('Pseudo Response [0].correct_option :', pseudo_response[0].correct_option, end='\n\n')

                    temp_counter = 0
                    for c_id in collect_id:               
                        response = request.POST.get(c_id)
                        # quiz = QuizModel.objects.get(pk=c_id)
                        quiz = QuizModel()
                        
                        email = User.objects.filter(id__exact=request.user.id).values('email')  ## Retrieving current user e-mail id from "User" Model
                        print('\nCurrent User Email :', email[0]['email'], end='\n')
                        quiz.poller = email[0]['email']  ## Storing current user e-mail id to Model
                        quiz.quiz_title = quiz_title

                        if poller_flag == 1:
                            quiz.user_id = request_id
                        else:
                            quiz.user = request.user  ## This is important becz the 'user' field in model cannot be Null.                

                    
                        if 'option' in response:                
                            print('\n\nMCQ Response', c_id, ':', response, end='\n\n')

                            if response == 'option1':                        
                                # quiz.option_one_count += 1
                                # quiz.option_one = 1                    #######################  Continue Stamp 1
                                quiz.correct_option = 1
                            if response == 'option2':
                                # quiz.option_two_count += 1
                                # quiz.option_one = 2
                                quiz.correct_option = 2
                            if response == 'option3':
                                # quiz.option_three_count += 1
                                # quiz.option_one = 3
                                quiz.correct_option = 3
                            if response == 'option4':
                                # quiz.option_four_count += 1                                                
                                # quiz.option_one = 4
                                quiz.correct_option = 4
                            if response == 'option5':
                                # quiz.option_five_count += 1
                                # quiz.option_one = 5
                                quiz.correct_option = 5
                            if response == 'option6':
                                # quiz.option_six_count += 1
                                # quiz.option_one = 6
                                quiz.correct_option = 6
                        else:
                            print('\n\nText Response', c_id, ':', response, end='\n\n')
                            quiz.correct_option = str(response)
                        
                        if pseudo_response[temp_counter].correct_option:
                            quiz.text_response = pseudo_response[temp_counter].correct_option                        
                        
                        temp_counter += 1

                        quiz.save()                    
                    messages.success(request, 'Your Response Is Recorded Successfully !!')
                    # redirect_path = 'http://127.0.0.1:8080/quiz/show_quiz/' + quiz_title
                    # return redirect(redirect_path)

                first_count = collect_id[0]
                context = { 'show_quiz': show_quiz, 'title': quiz_title, 'f_count': first_count }
                # print('\nIn Else\n')
                return render(request, 'quiz/show_quiz.html', context)                                

            else:
                show_quiz = QuizModel.objects.filter(poller__exact=quiz_title, user_id__exact=request_id)
                
                messages.info(request, "You've already attempted this survey !!")

                context = { 'show_quiz': show_quiz, 'title': quiz_title }
                return render(request, 'quiz/show_quiz.html', context)                

    else:
        return redirect('login')





def delete_quiz(request, quiz_title):
    if request.user.is_authenticated:

        quiz = QuizModel.objects.filter(quiz_title__exact = quiz_title)
        quiz.delete()

        return redirect('/quiz/get_titles/')

    else:
        return redirect('login')    



# myCtag_1 = []
# myCtag_2 = []
myCtag_1 = ''                        ######  Continue Stamp (June 16, 2021)
myCtag_2 = ''


def quiz_result(request, quiz_title):
    if request.user.is_authenticated:

        global myCtag_1, myCtag_2

        # For AnswerSheet (list of Correct Options) 
        correct_options = QuizModel.objects.filter(user_id__exact=request.user.id, quiz_title__exact=quiz_title, poller=quiz_title)
        print('\nCorrect Option: ', correct_options, end='\n\n')
        
        # For all distinct pollers(voters)
        pollers = QuizModel.objects.filter(user_id__exact=request.user.id, quiz_title__exact=quiz_title).exclude(poller=quiz_title).values('poller').distinct()
        print('\nPollers List :', pollers, end='\n\n')
        
        # myCtag.append(pollers)

        collect_pollers = []
        for p in pollers:
            print('Poller :', p['poller'])
            collect_pollers.append(p)

        print('\n\n')
        quiz_result = []     ## This will be a list of [Query Sets] of different "pollers".
        i = 0
        for cp in collect_pollers:
            print(i+1,'.', cp['poller'])    ## This technique ("cp['poller]") is used to to script(or extract) the values from "Objects" as we cannot access any value by "cp[0]" (gives error), so we used "cp['poller]" to extract the value associated with "poller" in this "cp" Object.
            temp_query_set = QuizModel.objects.filter(user_id__exact=request.user.id, quiz_title__exact=quiz_title, poller__exact=cp['poller'])
            temp_query_set = temp_query_set            
            quiz_result.append(temp_query_set)      # For the list of votes of each user
            print('Quiz Result :', quiz_result[i])
            i += 1

        print('\n\nQuiz Result (Full Set) :', quiz_result, end='\n\n')

        # global pollers_for_chart

        pollers_for_chart = QuizModel.objects.filter(user_id__exact=request.user.id, quiz_title__exact=quiz_title).exclude(poller=quiz_title)

        c_len = len(QuizModel.objects.filter(user_id__exact=request.user.id, quiz_title__exact=quiz_title, poller__exact=quiz_title))
        print('\nc_len :', c_len, end='\n\n')

        # myCtag_1.append(c_len)
        # myCtag_2.append(pollers_for_chart)

        myCtag_1 = c_len
        myCtag_2 = pollers_for_chart

        print('\nCorrect Options :', pollers_for_chart, end='\n\n')
        print('\nCorrect Options Length[len()] :', len(pollers_for_chart), end='\n\n')
        correct_counter = 0
        wrong_counter = 0
        neutral_counter = 0
        for cfp in pollers_for_chart:
            # print('\t', cfp.correct_option, '\n')
            if cfp.text_response != 'NULL':
                if cfp.text_response == cfp.correct_option:
                    correct_counter += 1
                else:
                    wrong_counter += 1

        print('\nCorrect Options (Counter) :', correct_counter, end='\n\n')
        print('\nWrong Options (Counter) :', wrong_counter, end='\n\n')


        # chart_data = [ 
            
        #     #["Accuracy", "Values"],
        #     [5, correct_counter],
        #     [5, wrong_counter]
         
        # ]                    


        context = { 'qresult' : quiz_result, 'correct_opt': correct_options, 'chart_correct': correct_counter, 'chart_wrong': wrong_counter }
        return render(request, 'quiz/quiz_result.html', context)


    else:
        return redirect('login')




def chart_stats_ctags_1():
    global myCtag_1    
    return myCtag_1

def chart_stats_ctags_2():
    global myCtag_2    
    return myCtag_2



def delete_response(request, quiz_title, poller):
    if request.user.is_authenticated:
        
        del_res = QuizModel.objects.filter(user_id__exact=request.user.id, quiz_title=quiz_title, poller=poller)
        print('\nResponse To Be Deleted:\n', del_res, end='\n\n')
        del_res.delete()    ## Do not write 'del_res.save()' after deleting the object('del_res.delete()').

        redirect_url = 'http://127.0.0.1:8080/quiz/quiz_result/' + quiz_title + '/'
        return redirect(redirect_url)

    else:
        return redirect('login')




# def share_quiz(request, quiz_title):
#     if request.user.is_authenticated:

#         # share_quiz = QuizModel.objects.filter(poller__exact=quiz_title)

#         quiz_title = 'pAcfizz' + str(request.user.id) + 'pAcfizz' + quiz_title
#         print('\nQuiz Title [Quiz Share] :', quiz_title, end='\n\n')

#         return show_quiz(request, quiz_title)

#     else:
#         return redirect('login')




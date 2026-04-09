from django import forms
from poll.models import PollModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PollForm(forms.ModelForm):

    state_option_four = forms.BooleanField(
        label = 'Add Option "Nota"',
        required = False
    )

    class Meta:
        model = PollModel
        fields = ['question', 'option_one', 'option_two', 'option_three', 'state_option_four']
        
        labels = {
            'question'          :  'Enter The Question Title',
            'option_one'        :  'Option 1',
            'option_two'        :  'Option 2',
            'option_three'      :  'Option 3',            
        }

        widgets = {
            'question'          :  forms.Textarea(attrs={'class':'form-control col-md-5', 'rows':'3'}),
            'option_one'        :  forms.TextInput(attrs={'class':'form-control col-md-3'}),
            'option_two'        :  forms.TextInput(attrs={'class':'form-control col-md-3'}),
            'option_three'      :  forms.TextInput(attrs={'class':'form-control col-md-3', 'style':'margin-bottom: 22px;'}),            
        }



class UserSignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username'  : forms.TextInput(attrs={'class':'form-control col-2'}),
            'first_name'  : forms.TextInput(attrs={'class':'form-control col-2'}),
            'last_name'  : forms.TextInput(attrs={'class':'form-control col-2'}),
            'email'  : forms.TextInput(attrs={'class':'form-control col-2'}),
        }
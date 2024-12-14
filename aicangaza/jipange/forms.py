from django import forms
from .models import Member, Contribution, Event 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']
#record a new contribution
class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount','date','member','event']

#create an event
class EventForm(forms.ModelForm):
    class Meta:
        model= Event
        fields = ['name', 'date','target','description' ]

# login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=TextInput())
                
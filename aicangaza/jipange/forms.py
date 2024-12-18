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
        fields = ['name', 'number', 'contact', 'mtaa']
#record a new contribution
class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount','date','member','event']
        widgets = {
            'event': forms.HiddenInput()
        }
        date = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Example format: Day/Month/Year (e.g., 18/12/2024)
        widget=forms.DateInput(attrs={'type': 'text'})  # Customize the input widget
    )

#create an event
class EventForm(forms.ModelForm):
    class Meta:
        model= Event
        fields = ['name', 'date','target','description' ]

        date = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Example format: Day/Month/Year (e.g., 18/12/2024)
        widget=forms.DateInput(attrs={'type': 'text'})  # Customize the input widget
    )

# login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=TextInput())
                
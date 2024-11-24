from django import forms
from .models import Member, Contribution, Event 

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['amount','date','member','event']

class EventForm(forms.ModelForm):
    class Meta:
        model= Event
        fields = ['name', 'date','target','description' ]
                
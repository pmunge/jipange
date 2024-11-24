from django.shortcuts import render, redirect
from .models import Member, Contribution
from .forms import MemberForm, ContributionForm, EventForm

# views to manage members and contributions
def member_list (request):
    members = Member.objects.prefetch_related('contributions_list').all()
    return render(request, 'jipange/member_list.html', {'members': members})

#functions that adds new members to jipange
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid ():
            form.save()
            return redirect('member_list')
    else:
            form = MemberForm()
    return render(request, 'jipange/add_member.html', {'form':form})
# function that adds member's contribution
def add_contribution( request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = Contribution()
    return render(request, 'jipange/add_contribution.html',{'form':form})

def member_contributions(request, member_id):
    member= Member.objects.get(id=member_id)  
    contributions = member.contributions.all()
    return render(request, 'jipange/member_contribution.html', {'member':member, 'contributions':contributions})              
 #function that adds an event 
def add_event(request):
    if request.method == 'POST':
         form = EventForm(request.POST)
         if form.is_valid ():
             form.save()
             return redirect('event_list')
    else:
            form = EventForm()
    return render(request, 'jipange/add_event.html', {'form':form})

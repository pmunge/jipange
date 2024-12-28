from django.shortcuts import render, redirect
from .models import Member, Contribution, Event
from .forms import MemberForm, ContributionForm, EventForm, LoginForm, CreateUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
#  . register
def register(request):
     form = CreateUserForm()
     if request.method == "POST":
          form = CreateUserForm(request.POST)
          if form.is_valid():
               form.save()

               return redirect('login')
     context = {'form':form}        
     return render(request, 'jipange/register.html', context=context)

#login users
def my_login(request):
     form =LoginForm()
     if request.method == "POST":
          form = LoginForm(request, data=request.POST)
          if form.is_valid():
               username = request.POST.get('username')
               password = request.POST.get('password')

               user =  authenticate(request, username=username, password=password)

               if user is not None:
                    auth.login(request,user)

                    return redirect('dashboard')
     context = {'form':form}
     return render(request, 'jipange/login.html', context=context) 
#user logout
def user_logout(request):
     auth.logout(request)
     return redirect("login")  

#...CRUD functions 
#dashboard view
@login_required(login_url = 'login')
def dashboard(request):
     return render(request, 'jipange/dashboard.html')           
# views to manage members and contributions
def contributionrecords (request):
    members = Member.objects.prefetch_related('contributions_list').exclude(contributions_list__isnull=True).all()
    return render(request, 'jipange/contributionrecords.html', {'members': members})


# 
              
 #function that dispalys the list of events and shows every contribution for each event

@login_required(login_url = 'login')
def event_list (request):
    events = Event.objects.all()
    for event in events:
        event.contributions = event.contributions_list.all()
    context = {'events': events}
    return render(request, 'jipange/event_list.html', context=context)

#creates a new event
def add_event(request):
    if request.method == 'POST':
         form = EventForm(request.POST)
         if form.is_valid ():
             form.save()
             return redirect('event_list')
    else:
            form = EventForm()
    return render(request, 'jipange/add_event.html', {'form':form})

# function that adds member's contribution to specific events
@login_required(login_url = 'login')
def event_contribution( request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution=form.save(commit=False)
            contribution.event = event
            contribution.save()
            return redirect('event_list')
    else:
        form = ContributionForm(initial={'event':event})
    return render(request, 'jipange/add_contribution.html',{'form':form, 'event': event})

@login_required(login_url = 'login')
def member_list (request, member_id):
    members = Member.objects.all()
    for member in members:
        member.contributions = member.contributions_list.all()
    context = {'members': members}
    return render(request, 'jipange/member_list.html', context=context)



def add_member(request):
    if request.method == 'POST':
         form = MemberForm(request.POST)
         if form.is_valid ():
             form.save()
             return redirect('member_list')
    else:
            form = MemberForm()
    return render(request, 'jipange/add_member.html', {'form':form})

@login_required(login_url = 'login')
def member_contribution( request, member_id):
    member = Member.objects.get(id=member_id)
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            contribution=form.save(commit=False)
            contribution.member = member
            contribution.save()
            return redirect('member_list', member_id=member.id)
    else:
        form = ContributionForm(initial={'member':member})
    return render(request, 'jipange/add_contribution.html',{'form':form, 'member': member})

# update members and events
#@login_required(login_url = 'login')
#def update (request):
    


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
#dashboard view
@login_required(login_url = 'login')
def dashboard(request):
     return render(request, 'jipange/dashboard.html')           
# views to manage members and contributions
def contributionrecords (request):
    members = Member.objects.prefetch_related('contributions_list').exclude(contributions_list__isnull=True).all()
    return render(request, 'jipange/contributionrecords.html', {'members': members})


# function that adds member's contribution
def add_contribution( request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contributionrecords.html')
    else:
        form = Contribution()
    return render(request, 'jipange/add_contribution.html',{'form':form})

def member_contributions(request, member_id):
    member= Member.objects.get(id=member_id)  
    contributions = member.contributions.all()
    return render(request, 'jipange/member_contribution.html', {'member':member, 'contributions':contributions})              
 #function that adds an event 
def event_list (request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'jipange/event_list.html', context=context)

def add_event(request):
    if request.method == 'POST':
         form = EventForm(request.POST)
         if form.is_valid ():
             form.save()
             return redirect('event_list')
    else:
            form = EventForm()
    return render(request, 'jipange/add_event.html', {'form':form})

def member_list (request):
    members = Member.objects.all()
    print("Members:", members)
    context = {'members': members}
    return render(request, 'jipange/member_list.html', context=context)

def add_member(request):
    if request.method == 'POST':
         form = MemberForm(request.POST)
         if form.is_valid ():
             form.save()
             print("New member saved!")
             return redirect('member_list')
    else:
            form = MemberForm()
    return render(request, 'jipange/add_member.html', {'form':form})



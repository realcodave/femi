from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.utils import timezone
# from .models import Agent, SubscriptionPlan, AgentSubscription, FeePayment
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  # Redirect to the desired page after login.
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
            return render(request, "index.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="index.html", context={"register_form":form})

def about_us(request):
    return render(request, "about-us.html")

def account_agency_management(request):
    return render(request, "account-agency-management.html")

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def contact_us(request):
    return render(request, "contact-us.ht,l")


@login_required
def agent_dashboard(request):
    return render(request, 'account-profile.html')
@login_required
def  account_agency_management(request):
    return render(request, 'account-agency-management.html')

@login_required
def purchase_subscription(request, subscription_plan_id):
    return redirect('agent_dashboard')

@login_required
def make_fee_payment(request):
    return render(request, 'make_payment.html')  # Create make_payment.html template
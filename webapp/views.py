from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateCustomerForm, UpdateCustomerForm, CreateEmploymentForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import customer, employment_details
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'webapp/index.html')

# User registration
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('user-login')
    context = {'registerForm': form}
    return render(request, 'webapp/user-register.html', context=context)

# User login
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect("user-dashboard")
    context = {'form':form}
    return render(request, 'webapp/user-login.html', context=context)


# User logout
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('user-login')

# User Dashboard
# Only logged in users can access this page
@login_required(login_url='user-login')
def dashboard(request):
    customer_data = customer.objects.all()
    context = {'customer_data': customer_data}
    return render(request, 'webapp/user-dashboard.html', context=context)

# Create a new customer
# Only logged in users can access this page
@login_required(login_url='user-login')
def createCustomer(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer created successfully')
            return redirect('user-dashboard')
    context = {'form': form}
    return render(request, 'webapp/customer-create.html', context=context)

# Update a customer
# Only logged in users can access this page
@login_required(login_url='user-login')
def updateCustomer(request, pk):
    customer_data = customer.objects.get(id=pk)
    form = UpdateCustomerForm(instance=customer_data)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=customer_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully')
            return redirect('customer-read', pk=pk)  # Redirect to the customer's details page
    context = {'form': form}
    return render(request, 'webapp/customer-update.html', context=context)

# Read single customer
# Only logged in users can access this page
@login_required(login_url='user-login')
def readCustomer(request, pk):
    all_records = customer.objects.get(id=pk)
    context = {'customer': all_records}
    return render(request, 'webapp/customer-read.html', context=context)

# Delete a customer
# Only superusers can delete customers
@login_required(login_url='user-login')
def deleteCustomer(request, pk):
    if not request.user.is_superuser:
        messages.error(request, 'Only superusers can delete customers.')
        return redirect('customer-read', pk=pk)  # Redirect to the customer's details page

    customer_data = customer.objects.get(id=pk)
    customer_data.delete()
    messages.success(request, 'Customer deleted successfully')
    return redirect('user-dashboard')

# Create employment details
# Only logged in users can access this page
@login_required(login_url='user-login')
def createEmployment(request, pk):
    customer_data = customer.objects.get(id=pk)
    form = CreateEmploymentForm()
    if request.method == 'POST':
        form = CreateEmploymentForm(request.POST)
        if form.is_valid():
            employment_data = form.save(commit=False)
            employment_data.customer = customer_data
            employment_data.save()
            messages.success(request, 'Employment details created successfully')
            return redirect('employment-read', pk=customer_data.id)  # Use customer_data.id instead of customer_id
    context = {'form': form}
    return render(request, 'webapp/employment-create.html', context=context)

# Read employment details
# Only logged in users can access this page
@login_required(login_url='user-login')
def readEmployment(request, pk):
    customer_data = customer.objects.get(id=pk)
    employment_data = employment_details.objects.filter(customer=customer_data)
    context = {'employment_data': employment_data, 'customer': customer_data}
    return render(request, 'webapp/employment-read.html', context=context)
 
# Delete employment details
# Only logged in users can access this page
@login_required(login_url='user-login')
def deleteEmployment(request, pk):
    employment_data = employment_details.objects.get(employment_id=pk)
    if request.method == 'POST':
        customer_id = employment_data.customer.id  # Get the customer's id
        employment_data.delete()
        messages.success(request, 'Employment details deleted successfully')
        return redirect('employment-read', pk=customer_id)  # Pass the customer's id to the redirect
    context = {'item': employment_data}
    return render(request, 'webapp/employment-delete.html', context=context)



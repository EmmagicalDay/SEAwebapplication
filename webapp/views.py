from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateCustomerForm, UpdateCustomerForm, CreateEmploymentForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import customer, employment_details
from django.urls import reverse
from django_otp.decorators import otp_required
from django_otp.plugins.otp_totp.models import TOTPDevice
import qrcode
from io import BytesIO
import base64


# Create your views here.

def home(request):
    return render(request, 'webapp/index.html')

# User registration
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            TOTPDevice.objects.create(user=user, name="default")
            messages.success(request, 'Account created successfully. Please set up your OTP device.')
            return redirect('user-login')
    context = {'registerForm': form}
    return render(request, 'webapp/user-register.html', context=context)

# Set up OTP
@login_required
def otp_setup(request):
    user = request.user
    device = TOTPDevice.objects.filter(user=user).first()
    if not device:
        device = TOTPDevice.objects.create(user=user, name="default")

    # Generate OTP QR code
    otp_uri = device.config_url
    qr = qrcode.make(otp_uri)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    context = {
        'qr_code': img_str,
        'otp_uri': otp_uri,
    }
    return render(request, 'webapp/otp-setup.html', context)

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
                auth_login(request, user)
                
                # OTP verification
                device = TOTPDevice.objects.filter(user=user).first()
                if device is None:
                    device = TOTPDevice.objects.create(user=user, name="default")
                
                request.session['otp_device_id'] = device.persistent_id
                return redirect('otp_verify')
            else:
                messages.error(request, 'Invalid credentials')
    
    context = {'form': form}
    return render(request, 'webapp/user-login.html', context=context)

@otp_required
def otp_verify(request):
    if request.method == 'POST':
        otp_code = request.POST.get('otp_code')
        device_id = request.session.get('otp_device_id')
        device = TOTPDevice.from_persistent_id(device_id)
        if device.verify_token(otp_code):
            return redirect('user-dashboard')
        else:
            messages.error(request, 'Invalid OTP code')
    
    return render(request, 'webapp/otp-verify.html')


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



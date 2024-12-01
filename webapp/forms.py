# Model forms for users that want to register and login

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import customer, employment_details


# User registration
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# User log in
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Create a new customer
class CreateCustomerForm(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = ['customer_first_name', 'customer_last_name', 'customer_date_of_birth', 'customer_gender', 'customer_employment_status']

# Update a customer
class UpdateCustomerForm(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = ['customer_first_name', 'customer_last_name', 'customer_date_of_birth', 'customer_gender', 'customer_employment_status']

# Create customer employment details
class CreateEmploymentForm(forms.ModelForm):
    
    class Meta:
        model = employment_details
        fields = ['employment_employer', 'employment_industry', 'employment_job_title', 'employment_salary', 'employment_pension_status']

    def clean_employment_salary(self):
    salary = self.cleaned_data.get('employment_salary')
    if salary is None or not isinstance(salary, (int, float)):
        raise forms.ValidationError("Salary must be a positive number.")
    if salary <= 0:
        raise forms.ValidationError("Salary must be a positive number.")
    return salary

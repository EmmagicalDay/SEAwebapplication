from django.test import TestCase
from webapp.forms import CreateUserForm, LoginForm, CreateCustomerForm, UpdateCustomerForm, CreateEmploymentForm
from webapp.models import customer, employment_details
from django.contrib.auth.models import User

class TestForms(TestCase):

# Tests for forms with valid data
    # Create a user to test the create user form
    def test_create_user_form_valid_data(self):
        form = CreateUserForm(data={
            'username': 'TestUser',
            'password1': 'randomWORDS258',
            'password2': 'randomWORDS258'
        })

        self.assertTrue(form.is_valid(), form.errors)

    # Create a user to test the login form
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser2',
            password='randomWORDS258'
        )

    # Test the login form with valid data
    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'username': 'TestUser2',
            'password': 'randomWORDS258'
        })

        self.assertTrue(form.is_valid(), form.errors)

    # Create a customer to test the create customer form
    def test_create_customer_form_valid_data(self):
        form = CreateCustomerForm(data={
            'customer_first_name': 'John',
            'customer_last_name': 'Doe',
            'customer_date_of_birth': '1980-01-01',
            'customer_gender': 'Male',
            'customer_employment_status': 'Active'
        })

        self.assertTrue(form.is_valid(), form.errors)

    # Update a customer to test the update customer form
    def test_update_customer_form_valid_data(self):
        form = UpdateCustomerForm(data={
            'customer_first_name': 'Johnathan',
            'customer_last_name': 'Doe',
            'customer_date_of_birth': '1980-01-01',
            'customer_gender': 'Male',
            'customer_employment_status': 'Active'
        })

        self.assertTrue(form.is_valid(), form.errors)

    # Create employment details to test the create employment form
    def test_create_employment_form_valid_data(self):
        form = CreateEmploymentForm(data={
            'employment_employer': 'Test Employer',
            'employment_industry': 'Healthcare',
            'employment_job_title': 'DR',
            'employment_salary': 50000,
            'employment_pension_status': 'E'
        })

        self.assertTrue(form.is_valid(), form.errors)

# Tests for forms with no data
    def test_create_user_form_no_data(self):
        form = CreateUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3, form.errors)

    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2, form.errors)

    def test_create_customer_form_no_data(self):
        form = CreateCustomerForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5, form.errors)

    def test_update_customer_form_no_data(self):
        form = UpdateCustomerForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5, form.errors)

    def test_create_employment_form_no_data(self):
        form = CreateEmploymentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5, form.errors)

# Test with missing data on one field
    def test_create_employment_form_invalid_data(self):
        form = CreateEmploymentForm(data={
            'employment_employer': '',
            'employment_industry': 'Test Industry',
            'employment_job_title': 'Test Job Title',
            'employment_salary': 50000,
            'employment_pension_status': 'Yes'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1, form.errors)

    # Test with incorrect data type
    def test_create_employment_form_invalid_salary(self):
        form = CreateEmploymentForm(data={
            'employment_employer': 'Test Employer',
            'employment_industry': 'Test Industry',
            'employment_job_title': 'Test Job Title',
            'employment_salary': 'invalid',  # salary should be a number
            'employment_pension_status': 'Yes'
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1, form.errors)
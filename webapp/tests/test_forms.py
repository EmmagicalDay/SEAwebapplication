from django.test import TestCase
from webapp.forms import (
    CreateUserForm,
    LoginForm,
    CreateCustomerForm,
    UpdateCustomerForm,
    CreateEmploymentForm,
)
from webapp.models import customer, employment_details  # Import models
from django.contrib.auth.models import User


class TestForms(TestCase):
    def setUp(self):
        # Create a user for testing login functionality
        self.user = User.objects.create_user(
            username="TestUser2", password="randomWORDS258"
        )

    # Tests for CreateUserForm
    def test_create_user_form_valid_data(self):
        form = CreateUserForm(
            data={"username": "ValidUser", "password1": "randomWORDS258", "password2": "randomWORDS258"}
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_create_user_form_invalid_data(self):
        # Missing all fields
        form = CreateUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3, form.errors)

    # Tests for LoginForm
    def test_login_form_valid_data(self):
        form = LoginForm(data={"username": "TestUser2", "password": "randomWORDS258"})
        self.assertTrue(form.is_valid(), form.errors)

    def test_login_form_invalid_data(self):
        # Missing both fields
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2, form.errors)

    # Tests for CreateCustomerForm
    def test_create_customer_form_valid_data(self):
        form = CreateCustomerForm(
            data={
                "customer_first_name": "John",
                "customer_last_name": "Doe",
                "customer_date_of_birth": "1980-01-01",
                "customer_gender": "Male",
                "customer_employment_status": "Active",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_create_customer_form_invalid_data(self):
        # Invalid gender and missing required fields
        form = CreateCustomerForm(
            data={
                "customer_first_name": "",
                "customer_last_name": "Doe",
                "customer_date_of_birth": "1980-01-01",
                "customer_gender": "InvalidGender",
                "customer_employment_status": "InvalidStatus",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4, form.errors)

    # Tests for UpdateCustomerForm
    def test_update_customer_form_valid_data(self):
        form = UpdateCustomerForm(
            data={
                "customer_first_name": "Johnathan",
                "customer_last_name": "Doe",
                "customer_date_of_birth": "1980-01-01",
                "customer_gender": "Male",
                "customer_employment_status": "Active",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_update_customer_form_invalid_data(self):
        # Missing all fields
        form = UpdateCustomerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6, form.errors)

    # Tests for CreateEmploymentForm
    def test_create_employment_form_valid_data(self):
        form = CreateEmploymentForm(
            data={
                "employment_employer": "Test Employer",
                "employment_industry": "Healthcare",
                "employment_job_title": "DR",  # Doctor
                "employment_salary": 50000.00,
                "employment_pension_status": "E",  # Enrolled
            }
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_create_employment_form_missing_data(self):
        # Missing employer and invalid choices
        form = CreateEmploymentForm(
            data={
                "employment_employer": "",
                "employment_industry": "InvalidIndustry",
                "employment_job_title": "InvalidTitle",
                "employment_salary": 50000.00,
                "employment_pension_status": "InvalidStatus",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5, form.errors)

    def test_create_employment_form_invalid_salary(self):
        # Invalid salary data type
        form = CreateEmploymentForm(
            data={
                "employment_employer": "Test Employer",
                "employment_industry": "Healthcare",
                "employment_job_title": "DR",
                "employment_salary": "NotANumber",  # Invalid data type
                "employment_pension_status": "E",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("employment_salary", form.errors)

    def test_create_employment_form_no_data(self):
        # Completely empty form
        form = CreateEmploymentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5, form.errors)

from django.test import TestCase
from webapp.models import customer, employment_details
from datetime import date
from django.core.exceptions import ValidationError

class CustomerModelTest(TestCase):

    def setUp(self):
        # Set up valid customer data for testing
        self.valid_customer_data = {
            'customer_first_name': 'John',
            'customer_last_name': 'Doe',
            'customer_date_of_birth': date(1990, 1, 1),
            'customer_gender': 'Male',  # Valid choice
            'customer_employment_status': 'Active'  # Valid choice
        }

    def test_customer_creation(self):
        # Test creating a customer with valid data
        customer_instance = customer.objects.create(**self.valid_customer_data)
        self.assertEqual(customer_instance.customer_first_name, 'John')
        self.assertEqual(customer_instance.customer_last_name, 'Doe')
        self.assertEqual(customer_instance.customer_date_of_birth, date(1990, 1, 1))
        self.assertEqual(customer_instance.customer_gender, 'Male')
        self.assertEqual(customer_instance.customer_employment_status, 'Active')

    def test_customer_creation_invalid_gender(self):
        # Test creating a customer with an invalid gender
        self.valid_customer_data['customer_gender'] = 'Invalid Gender'
        customer_instance = customer(**self.valid_customer_data)
        with self.assertRaises(ValidationError):
            customer_instance.full_clean()

    def test_customer_creation_invalid_employment_status(self):
        # Test creating a customer with an invalid employment status
        self.valid_customer_data['customer_employment_status'] = 'Invalid Status'
        customer_instance = customer(**self.valid_customer_data)
        with self.assertRaises(ValidationError):
            customer_instance.full_clean()

    def test_customer_creation_missing_name(self):
        # Test creating a customer with a missing first name
        self.valid_customer_data['customer_first_name'] = ''
        customer_instance = customer(**self.valid_customer_data)
        with self.assertRaises(ValidationError):
            customer_instance.full_clean()

class EmploymentDetailsModelTest(TestCase):

    def setUp(self):
        # Set up a customer and valid employment data for testing
        self.customer = customer.objects.create(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Male',
            customer_employment_status='Active'
        )
        self.valid_employment_data = {
            'customer': self.customer,
            'employment_employer': 'Test Employer',
            'employment_industry': 'IT',  # Valid choice
            'employment_job_title': 'SE',  # Valid choice
            'employment_salary': 50000,
            'employment_pension_status': 'E'  # Valid choice
        }

    def test_employment_creation(self):
        # Test creating employment details with valid data
        employment_instance = employment_details.objects.create(**self.valid_employment_data)
        self.assertEqual(employment_instance.customer, self.customer)
        self.assertEqual(employment_instance.employment_employer, 'Test Employer')
        self.assertEqual(employment_instance.employment_industry, 'IT')
        self.assertEqual(employment_instance.employment_job_title, 'SE')
        self.assertEqual(employment_instance.employment_salary, 50000)
        self.assertEqual(employment_instance.employment_pension_status, 'E')

    def test_employment_creation_invalid_industry(self):
        # Test creating employment details with an invalid industry
        self.valid_employment_data['employment_industry'] = 'Invalid Industry'
        employment_instance = employment_details(**self.valid_employment_data)
        with self.assertRaises(ValidationError):
            employment_instance.full_clean()

    def test_employment_creation_invalid_job_title(self):
        # Test creating employment details with an invalid job title
        self.valid_employment_data['employment_job_title'] = 'Invalid Job Title'
        employment_instance = employment_details(**self.valid_employment_data)
        with self.assertRaises(ValidationError):
            employment_instance.full_clean()

    def test_employment_creation_invalid_pension_status(self):
        # Test creating employment details with an invalid pension status
        self.valid_employment_data['employment_pension_status'] = 'Invalid Status'
        employment_instance = employment_details(**self.valid_employment_data)
        with self.assertRaises(ValidationError):
            employment_instance.full_clean()

    def test_employment_creation_missing_employer(self):
        # Test creating employment details with a missing employer
        self.valid_employment_data['employment_employer'] = ''
        employment_instance = employment_details(**self.valid_employment_data)
        with self.assertRaises(ValidationError):
            employment_instance.full_clean()

    def test_employment_creation_invalid_salary(self):
        # Test creating employment details with an invalid salary
        self.valid_employment_data['employment_salary'] = 'invalid'
        employment_instance = employment_details(**self.valid_employment_data)
        with self.assertRaises(ValidationError):
            employment_instance.full_clean()

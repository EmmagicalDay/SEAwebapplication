from django.test import TestCase
from webapp.models import customer, employment_details
from datetime import date

class CustomerModelTest(TestCase):

    # Create a customer to test the customer model
    def setUp(self):
        self.customer = customer.objects.create(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Male',
            customer_employment_status='Active'
        )

    # Test the customer model with valid data
    def test_customer_creation(self):
        self.assertEqual(self.customer.customer_first_name, 'John')
        self.assertEqual(self.customer.customer_last_name, 'Doe')
        self.assertEqual(self.customer.customer_date_of_birth, date(1990, 1, 1))
        self.assertEqual(self.customer.customer_gender, 'Male')
        self.assertEqual(self.customer.customer_employment_status, 'Active')

    # Test the customer model with invalid gender
    def test_customer_creation_invalid_gender(self):
        # Invalid gender should raise a ValueError
        with self.assertRaises(ValueError):
            customer.objects.create(
                customer_first_name='John',
                customer_last_name='Doe',
                customer_date_of_birth=date(1990, 1, 1),
                customer_gender='Invalid Gender',  # Invalid choice
                customer_employment_status='Active'
            )

    # Test the customer model with invalid employment status
    def test_customer_creation_invalid_employment_status(self):
        # Invalid employment status should raise a ValueError
        with self.assertRaises(ValueError):
            customer.objects.create(
                customer_first_name='John',
                customer_last_name='Doe',
                customer_date_of_birth=date(1990, 1, 1),
                customer_gender='Male',
                customer_employment_status='Invalid Status'  # Invalid choice
            )

    # Test the customer model with missing required fields (name)
    def test_customer_creation_missing_name(self):
        # Missing first name should raise an IntegrityError
        with self.assertRaises(Exception):  # Use Exception to catch IntegrityError
            customer.objects.create(
                customer_first_name='',
                customer_last_name='Doe',
                customer_date_of_birth=date(1990, 1, 1),
                customer_gender='Male',
                customer_employment_status='Active'
            )


class EmploymentDetailsModelTest(TestCase):

    # Create a customer and employment details to test the employment details model
    def setUp(self):
        self.customer = customer.objects.create(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Male',
            customer_employment_status='Active'
        )

        self.employment = employment_details.objects.create(
            customer=self.customer,
            employment_employer='Test Employer',
            employment_industry='IT',
            employment_job_title='SE',
            employment_salary=50000,
            employment_pension_status='E'
        )

    # Test the employment details model with valid data
    def test_employment_creation(self):
        self.assertEqual(self.employment.customer, self.customer)
        self.assertEqual(self.employment.employment_employer, 'Test Employer')
        self.assertEqual(self.employment.employment_industry, 'IT')
        self.assertEqual(self.employment.employment_job_title, 'SE')
        self.assertEqual(self.employment.employment_salary, 50000)
        self.assertEqual(self.employment.employment_pension_status, 'E')

    # Test the employment details model with invalid industry
    def test_employment_creation_invalid_industry(self):
        with self.assertRaises(ValueError):
            employment_details.objects.create(
                customer=self.customer,
                employment_employer='Test Employer',
                employment_industry='Invalid Industry',  # Invalid choice
                employment_job_title='SE',
                employment_salary=50000,
                employment_pension_status='E'
            )

    # Test the employment details model with invalid job title
    def test_employment_creation_invalid_job_title(self):
        with self.assertRaises(ValueError):
            employment_details.objects.create(
                customer=self.customer,
                employment_employer='Test Employer',
                employment_industry='IT',
                employment_job_title='Invalid Job Title',  # Invalid choice
                employment_salary=50000,
                employment_pension_status='E'
            )

    # Test the employment details model with invalid pension status
    def test_employment_creation_invalid_pension_status(self):
        with self.assertRaises(ValueError):
            employment_details.objects.create(
                customer=self.customer,
                employment_employer='Test Employer',
                employment_industry='IT',
                employment_job_title='SE',
                employment_salary=50000,
                employment_pension_status='Invalid Status'  # Invalid choice
            )

    # Test the employment details model with missing required fields (employer)
    def test_employment_creation_missing_employer(self):
        with self.assertRaises(Exception):  # Expect an IntegrityError or ValidationError
            employment_details.objects.create(
                customer=self.customer,
                employment_employer='',
                employment_industry='IT',
                employment_job_title='SE',
                employment_salary=50000,
                employment_pension_status='E'
            )

    # Test the employment details model with an invalid salary type
    def test_employment_creation_invalid_salary(self):
        with self.assertRaises(Exception):  # Invalid salary type (should be a decimal)
            employment_details.objects.create(
                customer=self.customer,
                employment_employer='Test Employer',
                employment_industry='IT',
                employment_job_title='SE',
                employment_salary="invalid",  # Invalid salary type
                employment_pension_status='E'
            )

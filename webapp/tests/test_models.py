from django.test import TestCase
from webapp.models import customer, employment_details
from datetime import date

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = customer.objects.create(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Male',
            customer_employment_status='Active'
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.customer_first_name, 'John')
        self.assertEqual(self.customer.customer_last_name, 'Doe')
        self.assertEqual(self.customer.customer_date_of_birth, date(1990, 1, 1))
        self.assertEqual(self.customer.customer_gender, 'Male')
        self.assertEqual(self.customer.customer_employment_status, 'Active')

    def test_customer_creation_invalid_gender(self):
        customer_instance = customer(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Invalid Gender',
            customer_employment_status='Active'
        )
        with self.assertRaises(ValueError):
            customer_instance.full_clean()

    def test_customer_creation_invalid_employment_status(self):
        customer_instance = customer(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Male',
            customer_employment_status='Invalid Status'
        )
        with self.assertRaises(ValueError):
            customer_instance.full_clean()

    def test_customer_creation_missing_name(self):
        customer_instance = customer(
            customer_first_name='',
            customer_last_name='Doe',
            customer_date_of_birth=date(1990, 1, 1),
            customer_gender='Male',
            customer_employment_status='Active'
        )
        with self.assertRaises(ValueError):
            customer_instance.full_clean()


class EmploymentDetailsModelTest(TestCase):

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

    def test_employment_creation(self):
        self.assertEqual(self.employment.customer, self.customer)
        self.assertEqual(self.employment.employment_employer, 'Test Employer')
        self.assertEqual(self.employment.employment_industry, 'IT')
        self.assertEqual(self.employment.employment_job_title, 'SE')
        self.assertEqual(self.employment.employment_salary, 50000)
        self.assertEqual(self.employment.employment_pension_status, 'E')

    def test_employment_creation_invalid_industry(self):
        employment_instance = employment_details(
            customer=self.customer,
            employment_employer='Test Employer',
            employment_industry='Invalid Industry',
            employment_job_title='SE',
            employment_salary=50000,
            employment_pension_status='E'
        )
        with self.assertRaises(ValueError):
            employment_instance.full_clean()

    def test_employment_creation_invalid_job_title(self):
        employment_instance = employment_details(
            customer=self.customer,
            employment_employer='Test Employer',
            employment_industry='IT',
            employment_job_title='Invalid Job Title',
            employment_salary=50000,
            employment_pension_status='E'
        )
        with self.assertRaises(ValueError):
            employment_instance.full_clean()

    def test_employment_creation_invalid_pension_status(self):
        employment_instance = employment_details(
            customer=self.customer,
            employment_employer='Test Employer',
            employment_industry='IT',
            employment_job_title='SE',
            employment_salary=50000,
            employment_pension_status='Invalid Status'
        )
        with self.assertRaises(ValueError):
            employment_instance.full_clean()

    def test_employment_creation_missing_employer(self):
        employment_instance = employment_details(
            customer=self.customer,
            employment_employer='',
            employment_industry='IT',
            employment_job_title='SE',
            employment_salary=50000,
            employment_pension_status='E'
        )
        with self.assertRaises(ValueError):
            employment_instance.full_clean()

    def test_employment_creation_invalid_salary(self):
        employment_instance = employment_details(
            customer=self.customer,
            employment_employer='Test Employer',
            employment_industry='IT',
            employment_job_title='SE',
            employment_salary="invalid",
            employment_pension_status='E'
        )
        with self.assertRaises(ValueError):
            employment_instance.full_clean()

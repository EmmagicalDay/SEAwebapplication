from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from webapp.models import customer, employment_details

# These tests will simulate POST requests to these views and then check the responses.

class ViewTestCase(TestCase):
    # Create a user and customer to test the views
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = customer.objects.create(
            customer_first_name='John',
            customer_last_name='Doe',
            customer_date_of_birth='1990-01-01',
            customer_gender='Male',
            customer_employment_status='Active'
        )
    # Test the home view
    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser2',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)
    
    # Test the login view with valid data
    def test_login(self):
        response = self.client.post(reverse('user-login'), {
            'username': 'testuser',
            'password': '12345',
        })
        self.assertEqual(response.status_code, 302)

    # Test the createCustomer view with valid data
    def test_createCustomer(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('customer-create'), {
            'customer_first_name': 'Jane',
            'customer_last_name': 'Doe',
            'customer_date_of_birth': '1990-01-01',
            'customer_gender': 'Female',
            'customer_employment_status': 'Active',
        })
        self.assertEqual(response.status_code, 302)

    # Test the createEmployment view with valid data
    def test_createEmployment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('employment-create', args=[self.customer.id]), {
            'employment_employer': 'Test Employer',
            'employment_industry': 'IT',
            'employment_job_title': 'SE',
            'employment_salary': 50000,
            'employment_pension_status': 'E',
        })
        self.assertEqual(response.status_code, 302)

    # Test createCustomer and createEmployment views with invalid data
    def test_createCustomer_invalid(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('invalid-customer-create'), {
            'customer_first_name': '',
            'customer_last_name': 'Doe',
            'customer_date_of_birth': '1990-01-01',
            'customer_gender': 'Female',
            'customer_employment_status': 'Active',
        })
        self.assertEqual(response.status_code, 200)  # The form should be re-rendered with errors

    def test_createEmployment_invalid(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('invalid-employment-create', args=[self.customer.id]), {
            'employment_employer': '',
            'employment_industry': 'IT',
            'employment_job_title': 'SE',
            'employment_salary': 50000,
            'employment_pension_status': 'E',
        })
        self.assertEqual(response.status_code, 200)  # The form should be re-rendered with errors
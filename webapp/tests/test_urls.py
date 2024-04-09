from django.urls import resolve
from django.test import SimpleTestCase
from webapp import views

class TestUrls(SimpleTestCase):

    # Test the URL resolution for each view
    def test_home_url_resolves(self):
        url = resolve('/')
        self.assertEqual(url.func, views.home)

    def test_register_url_resolves(self):
        url = resolve('/register')
        self.assertEqual(url.func, views.register)

    def test_login_url_resolves(self):
        url = resolve('/user-login')
        self.assertEqual(url.func, views.login)

    def test_logout_url_resolves(self):
        url = resolve('/user-logout')
        self.assertEqual(url.func, views.logout)

    def test_dashboard_url_resolves(self):
        url = resolve('/user-dashboard')
        self.assertEqual(url.func, views.dashboard)

    def test_createCustomer_url_resolves(self):
        url = resolve('/customer-create')
        self.assertEqual(url.func, views.createCustomer)

    def test_updateCustomer_url_resolves(self):
        url = resolve('/customer-update/1')
        self.assertEqual(url.func, views.updateCustomer)

    def test_readCustomer_url_resolves(self):
        url = resolve('/customer-read/1')
        self.assertEqual(url.func, views.readCustomer)

    def test_deleteCustomer_url_resolves(self):
        url = resolve('/customer-delete/1')
        self.assertEqual(url.func, views.deleteCustomer)

    def test_createEmployment_url_resolves(self):
        url = resolve('/customer/1/employment/create/')
        self.assertEqual(url.func, views.createEmployment)

    def test_readEmployment_url_resolves(self):
        url = resolve('/customer/1/employment/read/')
        self.assertEqual(url.func, views.readEmployment)

    def test_deleteEmployment_url_resolves(self):
        url = resolve('/employment/1/employment/delete/')
        self.assertEqual(url.func, views.deleteEmployment)

    # Test for nonexistent URLs
    def test_nonexistent_url_resolves(self):
        with self.assertRaises(Exception):
            url = resolve('/this-url-does-not-exist')

    def test_another_nonexistent_url_resolves(self):
        with self.assertRaises(Exception):
            url = resolve('/another-nonexistent-url')

    # Test for nonexistent URLs for failure
    def test_nonexistent_url_resolves(self):
        url = resolve('/this-url-does-not-exist')
        self.assertIsNotNone(url)

    def test_another_nonexistent_url_resolves(self):
        url = resolve('/another-nonexistent-url')
        self.assertIsNotNone(url)
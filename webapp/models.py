from django.db import models
from datetime import date

# Customer Model
class customer(models.Model):
    # Gender choices
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    # Employment status choices
    EMPLOYMENT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Parental Leave', 'Parental Leave'),
        ('Leaver', 'Leaver')
    ]

    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_date_of_birth = models.DateField(default=date(2000, 1, 1))
    customer_gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Prefer not to say')
    customer_employment_status = models.CharField(max_length=15, choices=EMPLOYMENT_STATUS_CHOICES, default='Active')
    customer_created = models.DateTimeField(auto_now_add=True)
    customer_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name}"

    # Validation logic
    def clean(self):
        # Validate gender
        if self.customer_gender not in dict(self.GENDER_CHOICES):
            raise ValueError(f"Invalid gender: {self.customer_gender}")
        
        # Validate employment status
        if self.customer_employment_status not in dict(self.EMPLOYMENT_STATUS_CHOICES):
            raise ValueError(f"Invalid employment status: {self.customer_employment_status}")

        # Ensure first and last name are provided
        if not self.customer_first_name:
            raise ValueError("First name is required.")
        if not self.customer_last_name:
            raise ValueError("Last name is required.")

# Employment Details Model
class employment_details(models.Model):
    # Industry choices
    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Retail', 'Retail'),
        ('Other', 'Other'),
    ]

    # Job title choices
    JOB_TITLE_CHOICES = [
        ('SE', 'Software Engineer'),
        ('DA', 'Data Analyst'),
        ('DS', 'Data Scientist'),
        ('PM', 'Project Manager'),
        ('WD', 'Web Developer'),
        ('DN', 'Dentist'),
        ('DR', 'Doctor'),
        ('NR', 'Nurse'),
        ('PH', 'Pharmacist'),
        ('TE', 'Teacher'),
        ('PR', 'Professor'),
        ('CO', 'Counselor'),
        ('AD', 'Administrator'),
        ('LI', 'Librarian'),
        ('FA', 'Financial Analyst'),
        ('AC', 'Accountant'),
        ('IB', 'Investment Banker'),
        ('FAD', 'Financial Advisor'),
        ('AU', 'Auditor'),
        ('SA', 'Sales Associate'),
        ('SM', 'Store Manager'),
        ('ME', 'Merchandiser'),
        ('BU', 'Buyer'),
        ('RA', 'Retail Analyst'),
        ('OT', 'Other'),
    ]

    # Pension status choices
    PENSION_STATUS_CHOICES = [
        ('E', 'Enrolled'),
        ('N', 'Not Enrolled')
    ]

    employment_employer = models.CharField(max_length=100)
    employment_industry = models.CharField(max_length=10, choices=INDUSTRY_CHOICES, default='Other')
    employment_job_title = models.CharField(max_length=3, choices=JOB_TITLE_CHOICES, default='OT')
    employment_salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_pension_status = models.CharField(max_length=1, choices=PENSION_STATUS_CHOICES, default='N')
    employment_created = models.DateTimeField(auto_now_add=True)
    employment_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employment_employer} - {self.employment_job_title}"

    # Validation logic
    def clean(self):
        # Validate industry choice
        if self.employment_industry not in dict(self.INDUSTRY_CHOICES):
            raise ValueError(f"Invalid industry: {self.employment_industry}")
        
        # Validate job title choice
        if self.employment_job_title not in dict(self.JOB_TITLE_CHOICES):
            raise ValueError(f"Invalid job title: {self.employment_job_title}")

        # Validate pension status choice
        if self.employment_pension_status not in dict(self.PENSION_STATUS_CHOICES):
            raise ValueError(f"Invalid pension status: {self.employment_pension_status}")

        # Ensure employer is not empty
        if not self.employment_employer:
            raise ValueError("Employer is required.")

        # Ensure salary is a valid number
        if self.employment_salary <= 0:
            raise ValueError("Salary must be a positive number.")

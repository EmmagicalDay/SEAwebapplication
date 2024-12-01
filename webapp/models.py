from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

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

    #customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_date_of_birth = models.DateField(default=date(2000, 1, 1))
    customer_gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Prefer not to say')
    customer_employment_status = models.CharField(max_length=15, choices=EMPLOYMENT_STATUS_CHOICES, default='Active')
    customer_created = models.DateTimeField(auto_now_add=True)
    customer_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name}"

    def clean(self):
        if self.customer_gender not in dict(self.GENDER_CHOICES):
            raise ValidationError(f"Invalid gender: {self.customer_gender}")
        if self.customer_employment_status not in dict(self.EMPLOYMENT_STATUS_CHOICES):
            raise ValidationError(f"Invalid employment status: {self.customer_employment_status}")
        if not self.customer_first_name:
            raise ValidationError("First name is required.")
        if not self.customer_last_name:
            raise ValidationError("Last name is required.")

class employment_details(models.Model):
    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Finance', 'Finance'),
        ('Retail', 'Retail'),
        ('Other', 'Other'),
    ]

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

    PENSION_STATUS_CHOICES = [
        ('E', 'Enrolled'),
        ('N', 'Not Enrolled')
    ]

    employment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    employment_employer = models.CharField(max_length=100)
    employment_industry = models.CharField(max_length=10, choices=INDUSTRY_CHOICES, default='Other')
    employment_job_title = models.CharField(max_length=3, choices=JOB_TITLE_CHOICES, default='OT')
    employment_salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_pension_status = models.CharField(max_length=1, choices=PENSION_STATUS_CHOICES, default='N')
    employment_created = models.DateTimeField(auto_now_add=True)
    employment_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employment_employer} - {self.employment_job_title}"

    def clean(self):
        errors = {}
        if self.employment_industry not in dict(self.INDUSTRY_CHOICES):
            errors['employment_industry'] = f"Invalid industry: {self.employment_industry}"
        if self.employment_job_title not in dict(self.JOB_TITLE_CHOICES):
            errors['employment_job_title'] = f"Invalid job title: {self.employment_job_title}"
        if self.employment_pension_status not in dict(self.PENSION_STATUS_CHOICES):
            errors['employment_pension_status'] = f"Invalid pension status: {self.employment_pension_status}"
        if not self.employment_employer:
            errors['employment_employer'] = "Employer is required."
        if self.employment_salary is None or self.employment_salary <= 0:
            errors['employment_salary'] = "Salary must be a positive number."

        if errors:
            raise ValidationError(errors)

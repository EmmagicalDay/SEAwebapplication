from django.db import models
from datetime import date

# Create your models here.

class customer(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Parental Leave', 'Parental Leave'),
        ('Leaver', 'Leaver')
    ]

    def clean(self):
        # Validate the gender choice
        if self.customer_gender not in dict(self.GENDER_CHOICES):
            raise ValueError(f"Invalid gender: {self.customer_gender}")

        # Validate the employment status choice
        if self.customer_employment_status not in dict(self.EMPLOYMENT_STATUS_CHOICES):
            raise ValueError(f"Invalid employment status: {self.customer_employment_status}")
    
    #customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_date_of_birth = models.DateField(default=date(2000, 1, 1))
    customer_gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Prefer not to say')
    customer_employment_status = models.CharField(max_length=15, choices=EMPLOYMENT_STATUS_CHOICES, default='A')
    customer_created = models.DateTimeField(auto_now_add=True)
    customer_updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.customer_first_name + ' ' + self.customer_last_name
    
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
            ('OT', 'Other')
    ]

    PENSION_STATUS_CHOICES = [
        ('E', 'Enrolled'),
        ('N', 'Not Enrolled')
    ]

    def clean(self):
        # Validate the industry choice
        if self.employment_industry not in dict(self.INDUSTRY_CHOICES):
            raise ValueError(f"Invalid industry: {self.employment_industry}")
        
        # Validate the job title choice
        if self.employment_job_title not in dict(self.JOB_TITLE_CHOICES):
            raise ValueError(f"Invalid job title: {self.employment_job_title}")
        
        # Validate the pension status choice
        if self.employment_pension_status not in dict(self.PENSION_STATUS_CHOICES):
            raise ValueError(f"Invalid pension status: {self.employment_pension_status}")
    
    employment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    employment_employer = models.CharField(max_length=100)
    employment_industry = models.CharField(max_length=10, choices=INDUSTRY_CHOICES, default='Other')
    employment_job_title = models.CharField(max_length=3, choices=JOB_TITLE_CHOICES, default='OT')
    employment_salary = models.DecimalField(max_digits=10, decimal_places=2)
    employment_pension_status = models.CharField(max_length=1, choices=PENSION_STATUS_CHOICES, default='N')
    employment_created = models.DateTimeField(auto_now_add=True)
    employment_updated = models.DateTimeField(auto_now=True)




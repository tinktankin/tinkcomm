from django.db import models

from app.models.base_model import BaseModel
from app.models.company import CompanyModel
from app.models.group import GroupModel


class SubscriberModel(BaseModel):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    )

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
        ('DUPLICATE', 'Duplicate')
    )

    company                 = models.ForeignKey(CompanyModel, verbose_name='Company', on_delete=models.CASCADE)
    full_name               = models.CharField(verbose_name='Full Name', max_length=255, null=True)
    first_name              = models.CharField(verbose_name='First Name', max_length=255)
    middle_name             = models.CharField(verbose_name='Middle Name', max_length=255, null=True)
    last_name               = models.CharField(verbose_name='Last Name', max_length=255)
    status                  = models.CharField(verbose_name='Susbcriber Status', choices=STATUS_CHOICES, max_length=10, default='ACTIVE')
    email                   = models.EmailField(verbose_name='Email Address', max_length=255)
    group                   = models.ManyToManyField(GroupModel)
    company_name            = models.CharField(verbose_name='Company Name', max_length=255, null=True)
    designation             = models.CharField(verbose_name='Designation', max_length=255, null=True)
    alternate_email         = models.EmailField(verbose_name='Alternate Email Address', max_length=255, null=True)
    phone_number            = models.CharField(verbose_name='Phone Number', max_length=30, null=True)
    alternate_phone_number  = models.CharField(verbose_name='Alternate Phone Number', max_length=30, null=True)
    city                    = models.CharField(verbose_name='City', max_length=255, null=True)
    address                 = models.CharField(verbose_name='Address', max_length=255, null=True)
    state                   = models.CharField(verbose_name='State', max_length=255, null=True)
    country                 = models.CharField(verbose_name='Country', max_length=255, null=True)
    zip_code                = models.CharField(verbose_name='Zip Code', max_length=255, null=True)
    gender                  = models.CharField(verbose_name='Gender', max_length=2, choices=GENDER_CHOICES, null=True)
    title                   = models.CharField(verbose_name='Title', max_length=255, null=True)
    department              = models.CharField(verbose_name='Department', max_length=255, null=True)
    university              = models.CharField(verbose_name='University', max_length=255, null=True)
    degree                  = models.CharField(verbose_name='Degree', max_length=255, null=True)
    passing_year            = models.CharField(verbose_name='Passing Year', max_length=255, null=True)
    college                 = models.CharField(verbose_name='College', max_length=255, null=True)
    industry                = models.CharField(verbose_name='Industry', max_length=255, null=True)
    key_skills              = models.CharField(verbose_name='Key Skills', max_length=255, null=True)
    total_exp               = models.CharField(verbose_name='Total Experience', max_length=255, null=True)
    years_business          = models.CharField(verbose_name='Years In Business', max_length=255, null=True)
    turnover                = models.CharField(verbose_name='Turnover', max_length=255, null=True)
    date_of_incorporation   = models.DateField(verbose_name='Incorporation Date', max_length=255, null=True)
    employees               = models.CharField(verbose_name='Employees', max_length=255, null=True)

    class Meta:
        unique_together = ('company', 'email', 'status')


    def __str__(self):
        return f"{self.email} - {self.company_id}"
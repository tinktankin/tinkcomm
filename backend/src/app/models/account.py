from django.db import models

from app.models.base_model import BaseModel
from app.models.company import CompanyModel

class AccountModel(BaseModel):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'None'),
    )

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
    )

    company             = models.ForeignKey(CompanyModel, verbose_name='Company', on_delete=models.CASCADE)

    first_name          = models.CharField(verbose_name='First Name', max_length=255)
    last_name           = models.CharField(verbose_name='Last Name', max_length=255)
    email               = models.EmailField(verbose_name='Email Address', max_length=255)
    password            = models.CharField(verbose_name='Password', max_length=255)
    gender              = models.CharField(verbose_name='Gender', max_length=2, choices=GENDER_CHOICES) 
    status              = models.CharField(verbose_name='Account Status', choices=STATUS_CHOICES, max_length=10)
    
    class Meta:
        unique_together = ('company', 'email')
    
    def __str__(self):
        return f"{self.email} - {self.company_id}"
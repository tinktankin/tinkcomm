from django.db import models

from app.models.base_model import BaseModel

class CompanyModel(BaseModel):

    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
        ('REGISTERED', 'Registered'),
    )

    
    name            = models.CharField(verbose_name='Company Name', max_length=225)
    code            = models.CharField(verbose_name='Company Code', max_length=10)
    status          = models.CharField(verbose_name='Company Status', choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.id} {self.name}"
from django.db import models

from app.models.base_model import BaseModel
from app.models.company import CompanyModel

class EmailModel(BaseModel):
    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETE', 'Complete'),
        ('ERROR', 'Error'),
    )

    company         = models.ForeignKey(CompanyModel, verbose_name='Company', on_delete=models.CASCADE)
    subject         = models.CharField(max_length=100)
    message         = models.CharField(max_length=1000)
    groups          = models.CharField(max_length=50, blank=True)
    subscribers     = models.CharField(max_length=50, blank=True)
    status          = models.CharField(verbose_name='Email Status', choices=STATUS_CHOICES, max_length=10)

    def __str__(self):
        return f"{self.company_id} {self.subject}"
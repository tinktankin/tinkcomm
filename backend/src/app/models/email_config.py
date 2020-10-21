from django.db import models

from app.models.base_model import BaseModel
from app.models.company import CompanyModel

class EmailConfigModel(BaseModel):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
    )

    company         = models.ForeignKey(CompanyModel, verbose_name='Company', on_delete=models.CASCADE)
    email_sender    = models.CharField(max_length=100)
    email_password  = models.CharField(max_length=30)
    smtp_server     = models.CharField(max_length=100)
    smtp_port       = models.PositiveIntegerField(default=587, blank=True)
    status          = models.CharField(verbose_name='Email Config Status', choices=STATUS_CHOICES, max_length=10, default='ACTIVE')

    class Meta:
        unique_together = ('company', 'email_sender')

    def __str__(self):
        return f"{self.company_id} {self.email_sender}"
from django.db import models

from app.models.base_model import BaseModel
from app.models.company import CompanyModel

class GroupModel(BaseModel):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
    )

    company = models.ForeignKey(CompanyModel, verbose_name='Company', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Group Name', max_length=225)
    description = models.CharField(verbose_name='Description', max_length=255, null=True)
    status = models.CharField(verbose_name='Company Status', choices=STATUS_CHOICES, max_length=10, default='ACTIVE')

    class Meta:
        unique_together = ('company', 'name')

    def __str__(self):
        return f"{self.id} {self.name}"
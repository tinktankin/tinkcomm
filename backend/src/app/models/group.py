from django.db import models

from app.models.base_model import BaseModel

class GroupModel(BaseModel):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'InActive'),
    )

    name = models.CharField(verbose_name='Group Name', max_length=225, unique=True)
    description = models.CharField(verbose_name='Description', max_length=255)
    status = models.CharField(verbose_name='Company Status', choices=STATUS_CHOICES, max_length=10, default='ACTIVE')

    def __str__(self):
        return f"{self.id} {self.name}"
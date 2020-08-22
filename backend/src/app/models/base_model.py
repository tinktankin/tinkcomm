from django.db import models


class BaseModel(models.Model):
    id                  = models.AutoField(primary_key=True)
    dateCreated         = models.DateTimeField(verbose_name='Date Created', auto_now_add=True) 
    dateModified        = models.DateTimeField(verbose_name='Date Modified', auto_now=True) 
    
    class Meta:
        abstract=True # Set this model as Abstract
    
    def __str__(self):
        return f"{self.id}"
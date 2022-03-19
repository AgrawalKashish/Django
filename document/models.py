from ctypes.wintypes import SIZE
from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    image=models.ImageField(blank=True, null=True)
class Meta:
    ordering = ('title',)
from django.db import models

# Create your models here.
from django.db import models

class Link(models.Model):
    date = models.CharField(max_length=100)
    test = models.CharField(max_length=100,default=0)
    scope = models.CharField(max_length=100,default=0)
    grade = models.TextField(blank=True)
    subject = models.IntegerField(default=0)

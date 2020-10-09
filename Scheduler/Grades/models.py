from django.db import models
from mainsite.models import User
import json

# Create your models here.
from django.db import models

class Link(models.Model):
    date = models.CharField(max_length=100)
    test = models.CharField(max_length=100,default=0)
    scope = models.CharField(max_length=100,default=0)
    grade = models.TextField(blank=True)
    subject = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

def set_grades_test_option(self, x):
    self.test = json.dumps(x)

def get_grades_test_option(self):
    return json.loads(self.test)

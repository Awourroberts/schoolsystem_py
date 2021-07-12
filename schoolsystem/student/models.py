from django.db import models
from django.db.models.fields import DateField
class student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=DateField()

# Create your models here.

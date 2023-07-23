from django.db import models
from django.urls import reverse
from django.db import IntegrityError,models,router,transaction

# Create your models here.

GENDER_CHOICES=[
    ('male','Male'),
    ('female','Female'),
    ('others','Others'),
]
class District(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=150, blank=True)
    date_Of_Birth = models.DateField(blank=True, null=True)
    age = models.IntegerField(max_length=150, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    phone_Number = models.IntegerField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    address = models.CharField(max_length=150,null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)
    account_Type= models.CharField(max_length=150,blank=True, null=True)
    materials_Provide = models.CharField(max_length=150, blank=True)
    def __str__(self):
        return self.name








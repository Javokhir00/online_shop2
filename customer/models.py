from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(region='UZ', blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    joined = models.DateTimeField()

    def __str__(self):
        return self.full_name
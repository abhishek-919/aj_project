from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class studentsdetails(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=False)
    DOB = models.DateField(blank=False)
    Mobilenumber = PhoneNumberField(blank=False)
    Emailid = models.EmailField(max_length=255, blank=False)
    Addressline1 = models.CharField(max_length=255, blank=False)
    Addressline2 = models.CharField(max_length=255, blank=False)
    District = models.CharField(max_length=255, blank=False)
    Postal_pincode = models.BigIntegerField(blank=False)
    mark_1 = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    mark_2 = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    mark_3 = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    mark_4 = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    mark_5 = models.IntegerField(blank=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    Total = models.IntegerField(blank=False)
    Average = models.DecimalField(max_digits=3, decimal_places=0)
    Registernumber = models.CharField(max_length=255, blank=False)






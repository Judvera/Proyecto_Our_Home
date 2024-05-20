from django.db import models
from django.utils.translation import gettext as _

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
    ]
    rut = models.CharField(max_length=9, primary_key=True, verbose_name=_('Rut'))
    first_name = models.CharField(max_length=100, verbose_name=_('Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    address = models.CharField(max_length=200, verbose_name=_('Address'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'))
    email = models.EmailField(verbose_name=_('Email'))
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, verbose_name=_('User Type'))
    password = models.CharField(max_length=128, default='1234562', verbose_name=_('Password'))
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Region(models.Model):
    name_region = models.CharField(max_length=100, verbose_name=_('Region'))

    def __str__(self):
        return self.name_region

class District(models.Model):
    name_district = models.CharField(max_length=100, verbose_name=_('District'))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='district')

    def __str__(self):
        return self.name_district

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('plot', 'Plot'),
    ]
    
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'))
    built_area = models.FloatField(verbose_name=_('Built Area'))
    total_area = models.FloatField(verbose_name=_('Total Area'))
    parking_spaces = models.IntegerField(verbose_name=_('Parking Spaces'))
    bedrooms = models.IntegerField(verbose_name=_('Bedrooms'))
    bathrooms = models.IntegerField(verbose_name=_('Bathrooms'))
    address = models.CharField(max_length=200, verbose_name=_('Address'))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_('Region'))
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name=_('District'))
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, verbose_name=_('Property Type'))
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Rental Price'))
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Landlord'))
    
    def __str__(self):
        return f'{self.name} - {self.landlord}'
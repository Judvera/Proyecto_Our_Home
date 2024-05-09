from django.db import models

class User(models.Model):
    USER_TYPE_CHOICES = [
        ('tenant', 'Tenant'),
        ('landlord', 'Landlord'),
    ]
    rut = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
class Region(models.Model):
    name_region = models.CharField(max_length=100)

    def __str__(self):
        return self.name_region

class District(models.Model):
    name_district = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='district')

    def __str__(self):
        return self.name_district

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('plot', 'Plot'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    built_area = models.FloatField()
    total_area = models.FloatField()
    parking_spaces = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)

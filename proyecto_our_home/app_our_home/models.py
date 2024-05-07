from django.db import models

# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICES = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    ]
    rut = models.CharField(max_length=9, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    built_area = models.FloatField()
    total_area = models.FloatField()
    parking_spaces = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    landlord = models.ForeignKey(User, on_delete=models.CASCADE)
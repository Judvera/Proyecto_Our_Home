import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_our_home.settings')
django.setup()

from app_our_home.models import Property

def list_properties_region():
    properties = Property.objects.values('name', 'description', 'region__name_region')
    with open('properties_region.txt', 'w') as file:
        for property in properties:
            line = f"{property['name']} - {property['description']} - Región: {property['region__name_region']}\n"
            file.write(line)

if __name__ == '__main__':
    list_properties_region()
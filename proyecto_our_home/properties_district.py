import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_our_home.settings')
django.setup()

from app_our_home.models import Property

def list_properties_district():
    properties = Property.objects.values('name', 'description', 'district__name_district')
    with open('properties_district.txt', 'w') as file:
        for property in properties:
            line = f"{property['name']} - {property['description']} - Comuna: {property['district__name_district']}\n"
            file.write(line)

if __name__ == '__main__':
    list_properties_district()
from .models import User, Property
from django.core.exceptions import ObjectDoesNotExist

def create_user(rut, first_name, last_name, address, phone, email, user_type):
    user = User(
        first_name=first_name, last_name=last_name, rut=rut, address=address,
        phone=phone, email=email, user_type=user_type)
    user.save()
    return user

def get_all_users():
    return User.objects.all()

def update_user(rut, **kwargs):
    try:
        user = User.objects.get(rut=rut)
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user
    except ObjectDoesNotExist:
        print(f"User with RUT {rut} not found.")
        return None
    
def delete_user(rut):
    try:
        user = User.objects.get(rut=rut)
        user.delete()
        print(f"User with RUT {rut} deleted.")
    except ObjectDoesNotExist:
        print(f"User with RUT {rut} not found.")
        
def create_property(
        name, description, built_area, total_area, parking_spaces,
        bedrooms, bathrooms, address, district, property_type,
        rental_price, landlord_rut):

    try:
        landlord = User.objects.get(rut=landlord_rut)

        property = Property(
            name=name,
            description=description,
            built_area=built_area,
            total_area=total_area,
            parking_spaces=parking_spaces,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            address=address,
            district=district,
            property_type=property_type,
            rental_price=rental_price,
            landlord=landlord
        )
        property.save()
        return property
    except User.DoesNotExist:
        print(f"Landlord with RUT {landlord_rut} not found.")
        return None

# Leer
def get_all_properties():
    return Property.objects.all()

# Actualizar
def update_property(property_id, **kwargs):
    try:
        property = Property.objects.get(id=property_id)
        for key, value in kwargs.items():
            setattr(property, key, value)
        property.save()
        return property
    except ObjectDoesNotExist:
        print(f"Property with ID {property_id} not found.")
        return None

# Eliminar
def delete_property(property_id):
    try:
        property = Property.objects.get(id=property_id)
        property.delete()
        print(f"Property with ID {property_id} deleted.")
    except ObjectDoesNotExist:
        print(f"Property with ID {property_id} not found.")
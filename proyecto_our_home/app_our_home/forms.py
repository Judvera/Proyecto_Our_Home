from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User, Property

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['rut', 'first_name', 'last_name', 'address', 'phone', 'email', 'user_type', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'built_area', 'total_area', 'parking_spaces', 'bedrooms', 'bathrooms', 'address', 'region', 'district', 'property_type', 'rental_price']


class PropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'built_area', 'total_area', 'parking_spaces', 'bedrooms', 'bathrooms', 'address', 'region', 'district', 'property_type', 'rental_price']
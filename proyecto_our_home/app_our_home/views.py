from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import login
from .forms import PropertyForm
from .models import Property
from .forms import PropertyUpdateForm

# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    return render(request, 'profile.html', {})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.landlord = request.user  # Asigna el arrendador actual como propietario
            property_instance.save()
            return redirect('home')  # Redirige a la página de inicio después de guardar la propiedad
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})

def update_property(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = PropertyUpdateForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio después de actualizar la propiedad
    else:
        form = PropertyUpdateForm(instance=property_instance)
    return render(request, 'update_property.html', {'form': form})

def delete_property(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        property_instance.delete()
        return redirect('home')  # Redirige a la página de inicio después de borrar la propiedad
    return render(request, 'delete_property.html', {'property': property_instance})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from .forms import PropertyForm, PropertyUpdateForm, UserRegistrationForm
from .models import User, Property

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

def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
            if password == user.password:
                # Login successful
                request.session['user_id'] = user.rut
                return redirect('profile')  # Redirect to a home page or dashboard
            else:
                # Invalid password
                error_message = 'Invalid password'
        except User.DoesNotExist:
            # User not found
            error_message = 'User not found'
    
    return render(request, 'registration/login.html', {'error_message': error_message})

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if not logged in
    
    user = User.objects.get(rut=user_id)
    return render(request, 'profile.html', {'user': user})

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
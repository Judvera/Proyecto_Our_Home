from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm, PropertyUpdateForm, UserRegistrationForm
from .models import User, Property, Region, District
from django.urls import reverse
from django.utils.translation import gettext as _

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
        email_username = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email_username)
            if check_password(password, user.password):
                request.session['user_id'] = user.rut
                request.session['user_email'] = user.email
                request.session['is_authenticated'] = True
                return redirect('profile')
            else:
                error_message = _('Invalid password')
        except User.DoesNotExist:
            user2 = authenticate(request, username=email_username, password=password)
            if user2 is not None:
                login(request, user2)
                return redirect('profile')
            else:
                error_message = _('Invalid email or password')
    
    return render(request, 'registration/login.html', {'error_message': error_message})

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_email']
        del request.session['is_authenticated']
    if request.user.is_authenticated:
        from django.contrib.auth import logout
        logout(request)
    return redirect('home')

def profile(request):
    try:
        user = User.objects.get(rut=request.session.get('user_id'))
    except User.DoesNotExist:
        user = request.user
    return render(request, 'profile.html', {'user': user})

def landlord_property(request):
    user = User.objects.get(rut=request.session.get('user_id'))
    if user.user_type != 'landlord':
        return redirect('profile')

    properties = Property.objects.filter(landlord=user)
    return render(request, 'landlord_property.html', {'properties': properties})

def add_property(request):
    user = User.objects.get(rut=request.session.get('user_id'))
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.landlord = user
            property.save()
            return redirect('landlord_property')
    else:
        form = PropertyForm()

    regions = Region.objects.all()
    districts = District.objects.all().order_by('name_district')

    return render(request, 'add_property.html', {
        'form': form,
        'regions': regions,
        'districts': districts,
    })
    
def update_property(request, property_id):
    user = User.objects.get(rut=request.session.get('user_id'))
    property = get_object_or_404(Property, id=property_id, landlord=user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, _('Property updated successfully!'))
            return redirect('landlord_property')
    else:
        form = PropertyForm(instance=property)

    regions = Region.objects.all()
    districts = District.objects.all().order_by('name_district')

    return render(request, 'update_property.html', {
        'form': form,
        'property': property,
        'regions': regions,
        'districts': districts,
    })

def delete_property(request, property_id):
    user = User.objects.get(rut=request.session.get('user_id'))
    property = get_object_or_404(Property, id=property_id, landlord=user)
    if request.method == 'POST':
        property.delete()
        messages.success(request, _('Property deleted successfully!'))
        return redirect('landlord_property')
    return render(request, 'confirm_delete_property.html', {'property': property})

def property_list(request):
    user = User.objects.get(rut=request.session.get('user_id'))
    
    regions = Region.objects.all()

    selected_region_id = request.GET.get('region')
    selected_district_id = request.GET.get('district')

    properties = Property.objects.all()
    
    if selected_region_id:
        properties = properties.filter(region_id=selected_region_id)
        
        districts = District.objects.filter(region_id=selected_region_id)
    else:
        districts = District.objects.none()

    if selected_district_id:
        properties = properties.filter(district_id=selected_district_id)

    return render(request, 'property_list.html', {
        'properties': properties,
        'regions': regions,
        'districts': districts,
        'selected_region_id': selected_region_id,
        'selected_district_id': selected_district_id,
    })
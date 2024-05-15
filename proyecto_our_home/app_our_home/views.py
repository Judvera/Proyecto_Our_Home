from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login

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

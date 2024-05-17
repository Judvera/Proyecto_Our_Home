from django.contrib.auth.hashers import make_password
from .models import User

def update_passwords():
    users = User.objects.filter(password='1234562')
    for user in users:
        user.password = make_password(user.password)
        user.save()
    print(f"Updated passwords for {len(users)} users")
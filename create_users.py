import time  # Import the time module
import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSWA.settings')
django.setup()

from accounts.models import CustomUser
from permissions.models import Role

def create_users():
    # Fetch all roles
    roles = list(Role.objects.all())

    for i in range(1, 101):  # Loop to create 100 users
        name = f"user{i}"
        email = f"user{i}@test.com"
        password = "1234"

        # Assign a random role
        role = random.choice(roles) if roles else None

        # Create the user
        user = CustomUser.objects.create_user(
            name=name,
            email=email,
            password=password,
            role=role
        )
        print(f"Created user: {name}, Email: {email}, Role: {role.name if role else 'No Role'}")
        time.sleep(0.1)  # Add a small delay for better visibility

if __name__ == '__main__':
    create_users()
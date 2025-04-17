import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSWA.settings')
django.setup()


import random
from permissions.models import Role, Permission

# Set up Django environment


# Fetch all permissions
perm_obj = Permission.objects.all()

# Define roles
roles = ['Project Manager', 'Principal Engineer', 'Senior Software Engineer', 'Junior Software Engineer', 'Trainee', 'CEO', 'CTO', 'COO']

for _ in range(100):
    # Select a random role
    role_name = random.choice(roles)
    
    # Get or create the role
    role, created = Role.objects.get_or_create(name=role_name)
    
    if role_name in ['CEO', 'Principal Engineer', 'Project Manager']:
        # Assign all permissions to these roles
        role.permissions.set(perm_obj)
        print(f"Assigned all permissions to role: {role_name}")
    else:
        # Assign a random subset of permissions to other roles
        random_permissions = random.sample(list(perm_obj), random.randint(1, len(perm_obj) - 1))
        role.permissions.set(random_permissions)
        print(f"Assigned random permissions to role: {role_name}")
    
    role.save()
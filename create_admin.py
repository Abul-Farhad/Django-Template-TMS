import time  # Import the time module
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSWA.settings')
django.setup()

from accounts.models import CustomUser
from permissions.models import Role, Permission

def create_admin_user():
    # Step 1: Create the 'admin' role
    role_name = 'Admin'
    admin_role, created = Role.objects.get_or_create(name=role_name)
    if created:
        print(f"Role '{role_name}' created.")
    else:
        print(f"Role '{role_name}' already exists.")
    
    # time.sleep(0.3)  # Add a 1-second delay

    # Step 2: Create all permissions (manually define them here)
    permissions = [
        {"name": "Can List Projects", "codename": "project-list"},
        {"name": "Can View Project Details", "codename": "project-detail"},
        {"name": "Can Create Project", "codename": "project-create"},
        {"name": "Can Update Project", "codename": "project-update"},
        {"name": "Can Delete Project", "codename": "project-delete"},
        {"name": "Can Generate Project Report", "codename": "project-report"},
        {"name": "Can List Users", "codename": "user-list"},
        {"name": "Can List Roles", "codename": "role-list"},
        {"name": "Can View Role Details", "codename": "role-detail"},
        {"name": "Can Create Role", "codename": "role-create"},
        {"name": "Can Update Role", "codename": "role-update"},
        {"name": "Can Delete Role", "codename": "role-delete"},
        {"name": "Can List Permissions", "codename": "permission-list"},
        {"name": "Can Assign Role to User", "codename": "assign-role"},
    ]

    for perm_data in permissions:
        permission, perm_created = Permission.objects.get_or_create(
            name=perm_data['name'],
            codename=perm_data['codename']
        )
        if perm_created:
            print(f"Permission '{perm_data['name']}' created.")
        else:
            print(f"Permission '{perm_data['name']}' already exists.")
        # Assign permission to the role
        admin_role.permissions.add(permission)
        # time.sleep(0.3)  # Add a 1-second delay for each permission
    print(f"All permissions assigned to role '{role_name}'.")
    # time.sleep(0.3)

    # Step 3: Create the superuser
    superuser_email = 'sakib@admin.com'
    superuser_password = 'admin'
    superuser_name = 'Sakib'

    if not CustomUser.objects.filter(email=superuser_email).exists():
        superuser = CustomUser.objects.create_superuser(
            email=superuser_email,
            password=superuser_password,
            name=superuser_name
        )
        superuser.role = admin_role  # Assign the role to the superuser
        superuser.save()
        print(f"Superuser '{superuser_email}' created and assigned role '{role_name}'.")
    else:
        print(f"Superuser with email '{superuser_email}' already exists.")
    # time.sleep(0.3)

if __name__ == '__main__':
    create_admin_user()
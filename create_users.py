# # import time  # Import the time module
# # import os
# # import django
# # import random

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSWA.settings')
# # django.setup()

# # from accounts.models import CustomUser
# # from permissions.models import Role
# # total_users = 5000000 - 100
# # def create_users():
# #     # Fetch all roles
# #     roles = list(Role.objects.all())
    
# #     for i in range(101, total_users):  # Loop to create 100 users
# #         name = f"user{i}"
# #         email = f"user{i}@test.com"
# #         password = "1234"

# #         # Assign a random role
# #         role = random.choice(roles) if roles else None

# #         # Create the user
# #         user = CustomUser.objects.create_user(
# #             name=name,
# #             email=email,
# #             password=password,
# #             role=role
# #         )
# #         # print(f"Created user: {name}, Email: {email}, Role: {role.name if role else 'No Role'}")
# #         # time.sleep(0.1)  # Add a small delay for better visibility

# # if __name__ == '__main__':
# #     create_users()
# #     print(f"All users created. Total users now: {total_users}")

# import os
# import django
# import random

# # Setup Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSWA.settings')
# django.setup()

# from django.db import connection
# from django.contrib.auth.hashers import make_password
# from permissions.models import Role

# total_users = 5000000 - 6000

# def create_users():
#     from django.utils.timezone import now

#     role_ids = list(Role.objects.values_list('id', flat=True))
#     batch_size = 10000
#     users = []

#     for i in range(6001, total_users + 1):
#         name = f"user{i}"
#         email = f"user{i}@test.com"
#         raw_password = "1234"
#         hashed_password = make_password(raw_password)

#         role_id = random.choice(role_ids) if role_ids else None

#         users.append((
#             name,
#             email,
#             hashed_password,
#             True if role_id == 1 else False,   # is_staff
#             False,   # is_active
#             True if role_id == 1 else False,   # is_superuser
#             role_id
#         ))

#         if len(users) >= batch_size:
#             insert_batch(users)
#             print(f"Inserted batch of {batch_size} users")
#             users = []

#     if users:
#         insert_batch(users)
#         print(f"Inserted final batch of {len(users)} users")


# def insert_batch(user_data):
#     with connection.cursor() as cursor:
#         values_list = [
#             val if isinstance(val := cursor.mogrify("(%s, %s, %s, %s, %s, %s, %s)", row), str) else val.decode("utf-8")
#             for row in user_data
#         ]
#         values = ",".join(values_list)
#         query = f"""
#             INSERT INTO accounts_customuser 
#             (name, email, password, is_staff, is_active, is_superuser, role_id)
#             VALUES {values}
#         """
#         cursor.execute(query)

# if __name__ == '__main__':
#     create_users()
#     print(f"All users created. Total users now: {total_users}")

import csv
import random
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FSWA.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from permissions.models import Role

roles = list(Role.objects.values_list('id', flat=True))  # List of role IDs
num_users = 5_000_000
curr_users = 2_000_000 + 1

# Pre-hash the static password only once
hashed_password = make_password("1234")

with open('bulk_users.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'role_id'])

    for i in range(curr_users + 1, num_users + 1):
        name = f"user{i}"
        email = f"user{i}@test.com"
        role_id = random.choice(roles)
        is_staff = is_superuser = role_id == 1
        is_active = False

        # Use pre-hashed password
        writer.writerow([name, email, hashed_password, is_staff, is_active, is_superuser, role_id])



    # \COPY accounts_customuser(name, email, password, is_staff, is_active, is_superuser, role_id)
    # FROM '/home/bs-01337/Projects/Tryng-Django-FSWA/FSWA/bulk_users.csv' DELIMITER ',' CSV HEADER;

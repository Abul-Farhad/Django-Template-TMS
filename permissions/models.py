from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField(Permission, related_name='roles')  # Many-to-Many relationship

    def __str__(self):
        return self.name
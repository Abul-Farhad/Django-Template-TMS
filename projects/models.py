from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=50, 
        default='Pending', 
        choices=[('Pending', 'Pending',), ('Development', 'Development'), ('Deployment', 'Deployment')])
    
    priority = models.CharField(
        max_length=50, 
        default='Low', 
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return self.title
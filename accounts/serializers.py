from rest_framework import serializers
from accounts.models import CustomUser



class ExportUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name', default='—')

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'is_staff', 'is_superuser', 'role']
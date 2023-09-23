from rest_framework import serializers
from .models import myuser

class myuserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = myuser
        fields = ('id', 'email','username', 'mobile_number',  'image','password')

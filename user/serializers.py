from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone', 'address', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True} 
        }
    
    def create(self, validated_data):
        """Hash password when creating user"""
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        """Hash password when updating user"""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    """Serializer for login endpoint"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email']).exists()
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if email_exists:
            raise ValidationError('email already exists')
        if username_exists:
            raise ValidationError('username already taken')
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.set_plain_password(password)
        user.save()

        return user

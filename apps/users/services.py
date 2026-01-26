
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def create_user(username, email, password):
    if User.objects.filter(username=username).exists():
        raise ValidationError("Username already exists")

    if len(password) < 6:
        raise ValidationError("Password too short")

    return User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
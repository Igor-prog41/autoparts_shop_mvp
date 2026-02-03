from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_register_data(username, password):
    if User.objects.filter(username=username).exists():
        raise ValidationError("Username already exists")

    if len(password) < 6:
        raise ValidationError("Password too short")


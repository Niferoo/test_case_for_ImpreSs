import re
from django.core.exceptions import ValidationError
from rest_framework import permissions


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Длина должна быть не менее 8 символов.')
    if not re.search(r'\d', value):
        raise ValidationError('Пароль должен иметь хотя бы одну цифру.')
    if not re.search(r'[A-Za-z]', value):
        raise ValidationError('Пароль должен содержать хотя бы одну букву.')


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'author'

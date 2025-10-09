from django.core.exceptions import ValidationError


def only_numbers(value):
    if not value.isdigit():
        raise ValidationError('This field must contain only numbers.')


def valid_cpf(value):
    if len(value) != 11:
        raise ValidationError('This field must contain exactly 11 digits.')


def valid_phone(value):
    if len(value) < 10:
        raise ValidationError('This field must contain at least 10 digits.')


def valid_zipcode(value):
    if len(value) != 8:
        raise ValidationError('This field must contain exactly 8 digits.')
from django.core.exceptions import ValidationError


def only_numbers(value):
    if not value.isdigit():
        raise ValidationError('This field must contain only numbers.')


def valid_cpf(value):
    if len(value) != 11 or value == value[0] * 11:
        raise ValidationError('Invalid CPF.')

    sum1 = sum(int(value[i]) * (10 - i) for i in range(9))
    digit1 = (sum1 * 10 % 11) % 10

    sum2 = sum(int(value[i]) * (11 - i) for i in range(10))
    digit2 = (sum2 * 10 % 11) % 10

    if int(value[9]) != digit1 or int(value[10]) != digit2:
        raise ValidationError('Invalid CPF.')


def valid_phone(value):
    if len(value) < 10:
        raise ValidationError('This field must contain at least 10 digits.')


def valid_zipcode(value):
    if len(value) != 8:
        raise ValidationError('This field must contain exactly 8 digits.')
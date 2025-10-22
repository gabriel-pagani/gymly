from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from .validators import valid_cpf, valid_phone, valid_zipcode


class Users(AbstractUser):
    STATES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    
    email = models.EmailField(unique=True, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True, validators=[valid_cpf])
    phone = models.CharField(max_length=11, blank=True, null=True, validators=[valid_phone])
    date_birth = models.DateField(blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    complement = models.CharField(max_length=200, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True, choices=STATES)
    zip_code = models.CharField(max_length=8, blank=True, null=True, validators=[valid_zipcode])
    observations = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Plans(models.Model):
    PAYMENTS_FREQUENCY = [
        (1, "Daily"),
        (7, "Weekly"),
        (30, "Monthly"),
        (60, "Bimonthly"),
        (90, "Quarterly"),
        (180, "Biannual"),
        (360, "Annual"),
    ]

    title = models.CharField(max_length=200, unique=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    payment_frequency = models.PositiveSmallIntegerField(choices=PAYMENTS_FREQUENCY, default=30)
    is_recurrent = models.BooleanField(default=True, verbose_name='Recurrent')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

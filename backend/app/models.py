from django.db import models
from django.core.validators import MinValueValidator


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
    observations = models.TextField(blank=True, null=True)
    recurrent = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

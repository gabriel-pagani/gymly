from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Q


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


class Contracts(models.Model):
    STATUS = [
        ("A", "Active"),
        ("P", "Pending"),
        ("L", "Locked"),
        ("I", "Inactive"),
        ("C", "Canceled"),   
    ]

    member = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, limit_choices_to=Q(groups__name="Members"), related_name="contracts")
    plan = models.ForeignKey(Plans, on_delete=models.PROTECT, limit_choices_to={"active": True}, related_name="subscriptions")
    start_date = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default="A")
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member} - {self.plan}"

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'


class Payments(models.Model): 
    STATUS = [ 
        ("P", "Pending"), 
        ("S", "Paid"),
        ("L", "Late"), 
        ("C", "Canceled"), 
        ("R", "Refunded"), 
    ]

    contract = models.ForeignKey(Contracts, on_delete=models.PROTECT, limit_choices_to=Q(status="A") | Q(status="P"), related_name="payments") 
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]) 
    expected_date = models.DateField() 
    payment_date = models.DateField(blank=True, null=True) 
    status = models.CharField(max_length=1, choices=STATUS, default="P")
    observations = models.TextField(blank=True, null=True) 
    
    def __str__(self): 
        return f"{self.expected_date} - {self.payment_date}" 
    
    class Meta: 
        verbose_name = 'Payment' 
        verbose_name_plural = 'Payments'

from django.contrib import admin
from .models import Plans, Contracts, Payments


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('title', 'payment_amount', 'payment_frequency', 'recurrent', 'active',)
    search_fields = ('title', 'observations',)
    list_filter = ('payment_frequency', 'recurrent', 'active',)


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'start_date', 'finish_date', 'status',)
    search_fields = ('observations',)
    list_filter = ('status',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('payment_amount', 'expected_date', 'payment_date', 'status',)
    search_fields = ('observations',)
    list_filter = ('status',)

from django.contrib import admin
from .models import Plans


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('title', 'payment_amount', 'payment_frequency', 'recurrent', 'active',)
    search_fields = ('title', 'observations',)
    list_filter = ('payment_frequency', 'recurrent', 'active',)

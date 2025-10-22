from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Users, Plans, Contracts, Payments


@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name', 'observations',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups',)
    filter_horizontal = ('groups', 'user_permissions',)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    ordering = ('email',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password',)
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'cpf', 'phone', 'date_birth',),
            'classes': ('collapse',)
        }),
        ('Address', {
            'fields': ('zip_code', 'state', 'city', 'neighborhood', 'street', 'number', 'complement',),
            'classes': ('collapse',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',), 
            'classes': ('collapse',)
        }),
        ('Dates', {
            'fields': ('last_login', 'date_joined',), 
            'classes': ('collapse',)
        }),
        ('Observations', {
            'fields': ('observations',), 
            'classes': ('collapse',)
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2',),
        }),
    )


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('title', 'payment_amount', 'payment_frequency', 'is_recurrent', 'is_active',)
    search_fields = ('title', 'observations',)
    list_filter = ('payment_frequency', 'is_active', 'is_recurrent',)
    ordering = ('title',)


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    list_display = ('member', 'plan', 'start_date', 'finish_date', 'status',)
    search_fields = ('observations',)
    list_filter = ('status',)
    ordering = ('member',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('payment_amount', 'expected_date', 'payment_date', 'status',)
    search_fields = ('observations',)
    list_filter = ('status',)
    ordering = ('-payment_date',)

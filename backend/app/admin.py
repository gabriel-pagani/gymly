from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from .models import Users, Dashboards, GroupDashboards


# Users Admin
@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'observations',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups',)
    filter_horizontal = ('groups', 'user_permissions', 'dashboards',)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    ordering = ('username',)
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password',)
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
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'dashboards',), 
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
            'fields': ('username', 'password1', 'password2',),
        }),
    )


# Groups Admin
admin.site.unregister(Group)
class GroupDashboardsInline(admin.StackedInline):
    model = GroupDashboards
    can_delete = False
    verbose_name_plural = 'Dashboards'
    filter_horizontal = ('dashboards',)
    fields = ('dashboards',)

class GroupsAdmin(BaseGroupAdmin):
    inlines = (GroupDashboardsInline,)
    
admin.site.register(Group, GroupsAdmin)


# Dashboards Admin
@admin.register(Dashboards)
class DashboardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'sector', 'status')
    search_fields = ('title', 'sector')
    filter_horizontal = ('fav_by',)
    list_filter = ('status', 'sector', 'fav_by')

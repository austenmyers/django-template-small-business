from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin, StackedInline

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile, ContactInfo, CustomerProfile, StaffProfile
from utils.fields import USAddress, UserPaymentCard, Position, PayRate, UserDocument, EmploymentEvent, ScheduledTime, DepositAccount, StaffAvailability


admin.site.unregister(Group)

class ProfileInline(StackedInline):
    model = Profile
    can_delete = False
    fieldsets = [
        ('Name', {
            'fields': [
                'first_name',
                'middle_name',
                'last_name',
            ]
        }),
        ('Profile Picture', {
            'fields': [
                'picture',
            ]
        })
    ]

class ContactInfoInline(StackedInline):
    model = ContactInfo
    can_delete = False

@admin.register(USAddress)
class USAddressAdmin(ModelAdmin):
    list_display = [
        'full_address',
        'user',
    ]

class CustomerProfileInline(StackedInline):
    model = CustomerProfile
    can_delete = False

admin.site.register(UserPaymentCard)

class StaffProfileInline(StackedInline):
    model = StaffProfile
    can_delete = False

admin.site.register(Position)
admin.site.register(PayRate)
admin.site.register(UserDocument)
admin.site.register(EmploymentEvent)
admin.site.register(ScheduledTime)
admin.site.register(DepositAccount)
admin.site.register(StaffAvailability)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    search_fields = [
        'email'
    ]
    ordering = [
        'email'
    ]
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = [
        'full_name',
        'email',
        'is_staff',
        'is_active',
    ]
    list_filter = [
        'email',
        'is_staff',
        'is_active',
    ]
    fieldsets = [
        (None, {
            'fields': [
                'email', 
                'password'
            ]
        }),
        ('Permissions', {
            'fields': [
                'is_staff', 
                'is_active', 
            ]
        }),
    ]
    add_fieldsets = [
        (None, {
            'fields': [
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ]
        })
    ]
    inlines = [
        ProfileInline,
        ContactInfoInline,
        CustomerProfileInline,
        StaffProfileInline,
    ]
    
    def full_name(self, user):
        from .utils import format_name

        return format_name(user, format='last, first MI')

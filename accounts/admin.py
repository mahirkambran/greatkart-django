from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django.utils.html import format_html
from .models import UserProfile

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



class UserProfileAdmin(admin.ModelAdmin):
    def thubnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius: 50px;" />'.format(object.profile_picture.url))
    thubnail.short_description = 'Profile Picture'
    list_display = ('user', 'thubnail', 'city', 'state', 'country')



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Account, AccountAdmin)

from django.contrib import admin
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)
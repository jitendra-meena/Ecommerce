from django.contrib import admin
from .models import User
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email','phone','is_superuser', 'is_active']

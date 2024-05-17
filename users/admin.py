from django.contrib import admin
from .models import UserAccount

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_staff')  # Liste des champs à afficher dans la section admin

admin.site.register(UserAccount, UserAccountAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Medico
from .forms import MedicoCreationForm, MedicoChangeForm

# Register your models here.

class MedicoAdmin(UserAdmin):
    add_form = MedicoCreationForm
    form = MedicoChangeForm
    model = Medico

    list_display = ['email', 'first_name', 'last_name', 'password', 'is_active', 'occupation']
    list_filter = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']

    fieldsets = (
        ('Campos do Modelo', {
            'fields': ('email', 'first_name', 'last_name', 'date_joined', 'password', 'occupation'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active'),
        }),
    )

    add_fieldsets = (
        ('Campos do Modelo', {
            'classes': ('wide', ),
            'fields': ('email', 'first_name', 'last_name', 'date_joined', 'password1', 'password2', 'is_staff', 'is_active', 'occupation')
        }),
    )

    search_fields = ('email', )
    ordering = ('email', )


admin.site.register(Medico, MedicoAdmin)

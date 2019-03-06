from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

class PerfilUsuarioInline(admin.StackedInline):
	model = PerfilUsuario
	can_delete = False

class UserAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline,)
    search_fields = ('username','email','first_name', 'last_name') 
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined',)
    ordering = ('-date_joined',)

    def get_queryset(self, request):
        queryset = super(UserAdmin, self).get_queryset(request)
        queryset = queryset.select_related('perfilusuario',)
        return queryset

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class CitaAdmin(admin.ModelAdmin):
    model = Cita
    list_display = ('paciente', 'created', 'estado')
    search_fields = ('paciente__name', 'id', )
    raw_id_fields = ['paciente', 'doctor']
admin.site.register(Cita, CitaAdmin)
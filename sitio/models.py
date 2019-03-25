from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField

# Create your models here.
class PerfilUsuario(models.Model):
    
    personal = 0
    paciente = 1
    doctor = 2

    TIPO_USUARIO = (
        (personal, 'Personal'),
        (paciente, 'Paciente'),
        (doctor, 'Doctor'),
    )

    direccion = models.TextField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    curp = models.CharField(max_length=20, blank=True)
    rfc = models.CharField(max_length=20, blank=True)
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_USUARIO, default=paciente)
    avatar = StdImageField(upload_to='usuarios/%Y/%m/',
                          variations={'perfil': {"width": 240, "height": 240, "crop": True}, 'thumbnail': {"width": 45, "height": 45, "crop": True} }, default="usuarios/avatar.png") 
    
    #Foreign Keys
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return u'Perfil de: %s' % self.user.username


class Cita(models.Model):
    pendiente = 0
    finalizada = 1

    ESTADO = (
        (pendiente, 'Pendiente'),
        (finalizada, 'Finalizada'),
    )

    dia_agendado = models.DateField(null=True, db_index=True)
    hora_agendado = models.TimeField(null=True)
    observacion = models.TextField(blank=True, null=True, default="")

    estado = models.PositiveSmallIntegerField(choices=ESTADO, default=pendiente)
    created = models.DateField(auto_now=True, editable=False)

    paciente = models.ForeignKey(User, related_name='user_cita', on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(User, related_name='user_doctor', on_delete=models.SET_NULL, null=True)
     
    def __str__(self):
        return u'%s' % self.id
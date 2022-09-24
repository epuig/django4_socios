from django.db import models
from localflavor.es.models import ESIdentityCardNumberField, ESPostalCodeField
from localflavor.es.es_provinces import PROVINCE_CHOICES
from datetime import date

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField("Nombre",max_length=50)
    apellidos = models.CharField("Apellidos",max_length=70)
    direccion = models.CharField(max_length=70)
    poblacion = models.CharField(max_length=70)
    codigo_postal = ESPostalCodeField(max_length=5)
    provincia =models.CharField(max_length=2, default="46",choices = PROVINCE_CHOICES)
    telefono_fijo = models.CharField(max_length=15, blank=True)
    telefono_movil = models.CharField(max_length=15)
    telefono_otro = models.CharField(max_length=15, blank=True)
    correo_electronico =models.EmailField(max_length=100, blank=True, default="")
    observaciones= models.TextField(max_length=250, blank=True)
    fecha_nacimiento = models.DateField("fecha de nacimiento", auto_now_add=False, null=True, blank=True, default=None)
    numero_socio = models.IntegerField(default=0)
   # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dni = ESIdentityCardNumberField()
    fecha_alta = models.DateField(blank=True, null=True, auto_now_add=False, default=None)
    fecha_baja = models.DateField(blank=True, null=True, auto_now_add=False, default=None)
    



    def __str__(self):
        return '%s, %s' % (self.apellidos, self.nombre)

    def get_age(self):
        today = date.today()
        dob= self.fecha_nacimiento
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
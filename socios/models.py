from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField("Nombre",max_length=50)
    apellidos = models.CharField("Apellidos",max_length=70)
    direccion = models.CharField(max_length=70)
    poblacion = models.CharField(max_length=70)
    codigo_postal =models.CharField(max_length=5)
    provincia =models.CharField(max_length=50, default="Valencia")
    telefono_fijo = models.CharField(max_length=15, blank=True)
    telefono_movil = models.CharField(max_length=15)
    telefono_otro = models.CharField(max_length=15, blank=True)
    correo_electronico =models.EmailField(max_length=100, blank=True, default="")
    observaciones= models.TextField(max_length=250, blank=True)

    def __str__(self):
        return '%s, %s' % (self.apellidos, self.nombre)
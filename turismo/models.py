from django.db import models

# Create your models here.
class Servicios(models.Model):
    id = models.AutoField(primary_key=True)  # Django crea automáticamente un campo id, así que esto es opcional.
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    foto = models.ImageField(upload_to='fotos_servicios/')
    descripción_del_lugar = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Servicio"         #Nombre singular del modelo
        verbose_name_plural = "Servicios" #Nombre plural del modelo
        ordering = ['precio']             #Orden por defecto al consultar la base de datos
                                          #verbose name = nombre detallado

    def __str__(self):
        return f"{self.descripción_del_lugar} - ${self.precio}"
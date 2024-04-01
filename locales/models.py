from django.db import models

class Comercio(models.Model):
    representante_legal = models.CharField(max_length =20)
    nombre_comercio = models.CharField(max_length =30)
    fecha_apertura = models.DateField()
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.representante_legal} {self.nombre_comercio} - {self.fecha_apertura}"

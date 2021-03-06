from django.db import models

class Articulo(models.Model):
    clave = models.CharField("Clave", max_length=30)
    nombre = models.CharField("Articulo", max_length = 150)
    descripcion = models.CharField("Descripcion", max_length = 300, blank=True, null=True)
    imagen = models.ImageField("Imagen", upload_to="articulos")
    precio = models.DecimalField("Precio unitario", max_digits=8, decimal_places=2)
    stock = models.IntegerField("Unidades")
    categoria = models.ForeignKey("articulos.Categoria", verbose_name="Categoria", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField("Categoria",max_length=100)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey("usuarios.Usuario", verbose_name="Usuario",on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.fecha

class DetalleVenta(models.Model):
    articulo = models.ForeignKey("articulos.Articulo", verbose_name="Articulo",on_delete=models.CASCADE)
    venta = models.ForeignKey("articulos.Venta",verbose_name="Venta",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.articulo.nombre+' '+self.venta.fecha.strftime('%d/%m/%Y')
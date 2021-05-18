from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class Usuario(User):
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.CASCADE)
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name="Municipio", on_delete=models.CASCADE)
    foto = models.ImageField("Foto de Perfil", upload_to='perfiles', blank=True, null=True)

class Estado(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre = models.CharField(max_length = 50)
    estado = models.ForeignKey('usuarios.Estado', verbose_name='Estado', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
def save_post(sender, instance, **kwargs):
    with open("logsUsuario.txt", "a+") as f:
        f.write("Se introdujo un nuevo usuario a la base de datos. \n")

def delete_post(sender, instance, **kwargs):
    with open("logsUsuario.txt", "a+") as f:
        f.write("Se eliminó un usuario de la base de datos. \n")

post_save.connect(save_post, sender=Usuario)
post_delete.connect(delete_post, sender=Usuario)

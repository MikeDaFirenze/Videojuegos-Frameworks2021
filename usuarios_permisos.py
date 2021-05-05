import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','videojuego.settings')
django.setup()

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario

# Creacion de permisos

# Grupos
#grupo_administradores = Group.objects.create(name='administradores')
#grupo_usuarios = Group.objects.create(name='usuarios')


content_type = ContentType.objects.get_for_model(Usuario)

#permiso_usuarios = Permission.objects.create(
#    codename = 'permiso_usuarioss',
#    name = 'Permiso requerido para el grupo Usuarios',
#    content_type = content_type
#)

#permiso_administradores = Permission.objects.create(
#    codename = 'permisos_administradoress',
#    name = 'Permiso requerido para administradores',
#    content_type = content_type
#)

permiso_gestion_permisos = Permission.objects.create(
    codename = 'permiso_gestion_permisos',
    name = 'Permiso para administrar permisos en los otros usuarios',
    content_type = content_type
)

#grupo_usuarios.permissions.add(permiso_usuarios)
#grupo_administradores.permissions.add(permiso_administradores)
grupo_administradores.permissions.add(permiso_gestion_permisos)

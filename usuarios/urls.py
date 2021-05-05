from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('lista/', views.UsuariosList.as_view(), name='lista'),
    path('nuevo/', views.NuevoUsuario.as_view(), name='nuevo'),
    path('pdf/', views.UsuariosPdf.as_view(), name='pdf'),
    path('Updf/<int:pk>', views.UsuarioPdf.as_view(), name='Updf'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
   #path('activar/', views.form_valid.as_view(), name='activar'),
    path('signup/', views.SignupUsuario.as_view(), name='signup'),
    path('municipios/', views.obtiene_municipios, name='municipios'),
    path('permisos/<int:pk>', views.Permisos.as_view(), name='permisos'),
    path('eliminar/<int:id>', views.EliminarUsuario, name='eliminar'),
    
]

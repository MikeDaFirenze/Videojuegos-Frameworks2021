from django.urls import path
from . import views

app_name = 'categoria'

urlpatterns = [
    path('lista/', views.lista_categorias, name='lista'),
    path('eliminar/<int:id>', views.eliminar_categorias, name='eliminar'),
    path('alta/', views.nueva_categoria, name='alta'),
    path('editar/<int:id>', views.editar_categoria, name='editar'),
    
]

from django.urls import path
from . import views

app_name = 'videojuego'

urlpatterns = [
    
    #### Clases #####
    path('listacl/', views.VideojuegoList.as_view(), name='listacl'),
    path('eliminarcl/<int:pk>', views.VideojuegoDelete.as_view(), name='eliminarcl'), #En clase usar pk en lugar de id
    path('altacl/', views.VideojuegoCrear.as_view(), name='altacl'),   
    path('editarcl/<int:pk>', views.VideojuegoActualizar.as_view(), name='editarcl'), 
    path('vercl/<int:pk>', views.VideojuegoDetalle.as_view(), name='vercl'), 
]

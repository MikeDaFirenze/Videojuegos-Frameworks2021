from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Videojuego
from .forms import CategoriaForm, VideojuegoForm

from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

###### Categorías ###### 
def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias, "cat_lista":True}
    return render(request, 'lista_categorias.html', context)

def eliminar_categorias(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    
    return redirect('categoria:lista')

def nueva_categoria(request):
    form = CategoriaForm()
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')

    context = {'form' : form, "cat_nueva":True}
    return render(request, 'alta_categoria.html', context)

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(instance=categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
    context = {'form' : form, "cat_edit":True}
    return render(request, 'editar_categoria.html', context)




###### Videojuegos ######

def lista_videojuegos (request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'lista_videojuegos.html', {'videojuegos':videojuegos})

def eliminar_videojuegos(request, id):
    videojuego = Videojuego.objects.get(id = id)
    videojuego.delete()
    return redirect('videojuego:lista')

def nuevo_videojuego(request):
    form = VideojuegoForm()
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videojuego:lista')

    context = {'form' : form}
    return render(request, 'alta_videojuego.html', context)

def editar_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    form = VideojuegoForm(instance=videojuego)
    if request.method == 'POST':
        form = Videojuego(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('videojuego:lista')
    context = {'form' : form}
    return render(request, 'editar_videojuego.html', context)



#### Videojuego Clase #######

class VideojuegoList(ListView):
    model = Videojuego
    paginate_by = 5
    context_object_name = 'videojuegos'
    extra_context = {'etiqueta':'Lista', 'vj_lista':True}
   

class VideojuegoDelete(DeleteView):
    model = Videojuego
    
    success_url = reverse_lazy('videojuego:listacl')
    extra_context = {'etiqueta':'Eliminar', 'vj_del':True}

class VideojuegoCrear(CreateView):
    model = Videojuego
    form_class = VideojuegoForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'vj_nuevo':True}
    success_url = reverse_lazy('videojuego:listacl')

class VideojuegoActualizar(UpdateView):
    model = Videojuego
    form_class = VideojuegoForm
    extra_context = {'etiqueta':'Actualizar', 'boton':'Guardar', 'vj_edit':True}
    success_url = reverse_lazy('videojuego:listacl')

class VideojuegoDetalle(DetailView):
    model = Videojuego
    extra_context = {'etiqueta':'Detalles', 'boton':'Regresar', 'vj_det':True}
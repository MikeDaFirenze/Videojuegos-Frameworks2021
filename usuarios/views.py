from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User, Group, Permission
from .models import Usuario, Municipio, Estado
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django_weasyprint import WeasyTemplateResponseMixin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin
""" from django.contrib.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .token import token_activacion
from django.core.mail import EmailMessage """
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from django.core.signals import request_finished

request_signal_del = Signal(providing_args=['id'])
request_signal_add = Signal(providing_args=['id'])

class NuevoUsuario(PermissionRequiredMixin, CreateView):
    permission_required = 'usuarios.add_usuario'
    model = Usuario
    form_class = UsuarioForm
    extra_context = {'etiqueta':'Nuevo', 'boton':'Agregar', 'nuevo_user':True}
    success_url = reverse_lazy('usuarios:lista')
    

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        request_signal_add.send(sender=Usuario, id=user.id)
        
        


        """ dominio = get_current_site(self.request)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)

        mensaje = render_to_string('confirmar_cuenta.html',
            {
                'usuario': user,
                'dominio': dominio,
                'uid': uid,
                'token': token
            }
        ) 
        asunto = 'Activa cuenta videojuegos'
        to = user.email
        email = EmailMessage(
            asunto,
            mensaje,
            to=[to]
        )
        email.content_subtype = 'html'
        email.send() """

        return super().form_valid(form)

class UsuariosList(PermissionRequiredMixin, ListView):
    permission_required = 'usuarios.view_usuario'
    model = Usuario
    paginate_by = 5
    context_object_name = 'usuarios'
    extra_context = {'etiqueta':'Lista', 'user_lista':True}

def EliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    request_signal_del.send(sender=Usuario, id=id)
    usuario.delete()
    return redirect('usuarios:lista')

class Permisos(PermissionRequiredMixin, ListView):
    permission_required = 'usuarios.change_permission'
    model = Usuario
    template_name = 'usuarios/permisos.html'
    success_url = reverse_lazy('usuarios:lista')
    
    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk',None)
        usr = Usuario.objects.get(id = pk)
        queryset = [(x.name) for x in Group.objects.filter(user=usr)]
        return queryset

class LoginUsuario(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):

        self.request.session['cuantos'] = 0
        self.request.session['total'] = 0.0
        self.request.session['articulos'] = {}

        return super().get_success_url()
    
    success_url = reverse_lazy('usuarios:lista')

class VistaPdf(ListView):
    model = Usuario
    context_object_name = 'usuarios'
    template_name = 'usuarios/usuarios_pdf.html'

class UsuariosPdf(WeasyTemplateResponseMixin, VistaPdf):
    model = Usuario
    #pdf_attachment = True
    pdf_filename = 'Lista_usuarios.pdf'

    

class VistaPdf2(ListView):
    model = Usuario
    #context_object_name = 'object'
    template_name = 'usuarios/usuario_pdf.html'

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk',None)
        queryset = Usuario.objects.filter( id = pk)
        print(queryset)
        return queryset
    

class UsuarioPdf(WeasyTemplateResponseMixin, VistaPdf2):
    #pdf_attachment = False
    pdf_filename = 'Usuario.pdf'



class SignupUsuario(CreateView):
    template_name = 'signup.html'
    model = Usuario
    form_class = UsuarioForm
    def agregado(self):
        ultimo = Usuario.objects.last()
        request_signal_add.send(sender=Usuario, id=ultimo.id)
    success_url = reverse_lazy('usuarios:login')


def obtiene_municipios(request):
    if request.method == 'GET':
        return JsonResponse({'error':'Petición incorrecta'}, safe=False,  status=403)
    id_estado = request.POST.get('id')
    municipios = Municipio.objects.filter(estado_id=id_estado)
    json = []
    if not municipios:
        json.append({'error':'No se encontraron municipios para ese estado'})
    for municipio in municipios:
        json.append({'id':municipio.id, 'nombre':municipio.nombre})
    return JsonResponse(json, safe=False)

@receiver(request_finished)
def post_request_receive(sender, **kwargs):
    with open("logsRequests.txt", "a+") as f:
        f.write("Un usuario ingresó a la página de lista usuarios. \n")

@receiver(request_signal_del)
def post_delete_user_request(sender, **kwargs):
    with open("logsRequestsChidos.txt", "a+") as f:
        f.write(f"El usuario con el id: {kwargs['id']}, fue eliminado de la lista usuarios. \n")

@receiver(request_signal_add)
def post_add_user_request(sender, **kwargs):
    with open("logsRequestsChidos.txt", "a+") as f:
        f.write(f"Un nuevo usuario con el id: {kwargs['id']}, ha sido registrado en la lista usuarios. \n")

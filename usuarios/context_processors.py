from .models import Usuario
from django.contrib.auth.models import Group

def total_permisos(request):
    queryset = [(x.name) for x in Group.objects.all()]
    kwargs = {
        'total_permisos' : queryset
    }

    return kwargs
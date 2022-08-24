from multiprocessing import context
from django.shortcuts import render
from .models import miembros


# Create your views here.
def principal(request):
   nombre = miembros.objects.create(nombre = "Jorge",saldo = 1000000, fecha_nac = "1958-09-05")
   context = {'miembro':miembros}


   return render(request, 'principal.html', context={})

#def ver_familiares(request):
#     miembro= miembros.objects.all()
#     context = {'miembro': miembros, }
#     return render(request, "lista.html", context={})
     
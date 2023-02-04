from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tecido
#from .models import Usuario

def index(request):
  if request.method == "GET": 
    tecidos = Tecido.objects.all()
    return render(request, 'core/index.html', {'tecidos':tecidos})

def estoque(request):
    tecidos = Tecido.objects.all()
    return render(request, 'core/estoque.html', {'tecidos':tecidos})
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tecido, TIPOS_TECIDO, CORES
from django.db.models import Sum
#from .models import Usuario

def index(request):
  if request.method == "GET": 
    tecidos = Tecido.objects.all()
    tecidos = tecidos.order_by('id')
    tipos_tecido = list(TIPOS_TECIDO)
    cores = list(CORES)
    filtros = {"Tipo de tecido":1,"Cor":2,"Estoque":3}
    filtro_selecionado= request.GET.get('filtro_selecionado')
    if filtro_selecionado == "1":
      tecidos=tecidos.order_by('tipo')
    if filtro_selecionado == "2":
      tecidos=tecidos.order_by('cor')
    if filtro_selecionado == "3":
      tecidos=tecidos.order_by('metros')
    return render(request, 'core/index.html', {'tecidos':tecidos, 'tipos_tecido': tipos_tecido, 'cores': cores, 'filtros':filtros})
  elif request.method =="POST":
    tipo = request.POST.get('tipo')
    cor = request.POST.get('cor')
    metros = request.POST.get('metros')
    tecido = Tecido(
      tipo=tipo,
      cor=cor,
      metros=metros
    )
    tecido.save()
    return redirect('/')



def producao(request):
    tecidos = Tecido.objects.all()
    proportion = 7
    bones_totais = 0
    for bones in tecidos:
      bones_totais+=bones.metros
    bones_totais=bones_totais*proportion
    #for bones in metros_totais:

    return render(request, 'core/estoque.html', {'tecidos':tecidos, 'proportion':proportion, 'bones_totais':bones_totais})


def excluir(request, id):
    tecido = Tecido.objects.get(id=id)
    tecido.delete()
    #messages.add_message(request, constants.SUCCESS, 'Empresa excluída com sucesso')
    return redirect('/')

def alterar(request, id):
    tecido = Tecido.objects.get(id=id)
    tecido.metros = tecido.metros + 1
    tecido.save()
    return redirect('/')

def subtrair_estoque(request, id):
    tecido = Tecido.objects.get(id=id)
    tecido.metros = tecido.metros - 1
    if tecido.metros == 0:
        tecido.save()
        tecido.delete()
    else:
        tecido.save()
    return redirect('/')
from django.shortcuts import render, redirect
from site1.models import produto


def pagina_inicial(request):
    form = produto.objects.all()

    return render (request, 'html/page_main.html',{'produto':form})

def comprar(request, comprar_pk):

    comprando = produto.objects.get(pk=comprar_pk)

    return render (request, 'html/comprar_main.html',{'comprando':comprando})

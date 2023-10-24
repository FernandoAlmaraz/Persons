from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bienvenido(request):
    return HttpResponse("Hola a todos")


def despedida(request):
    return HttpResponse("Adios a todos")


def contacto(resque):
    return HttpResponse("Celular: 77999469- Email: fercho@gmail.com")

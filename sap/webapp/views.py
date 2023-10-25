from django.shortcuts import render
from django.http import HttpResponse

from persons.models import Person


# Create your views here.
# def bienvenido(request):
#     mensajes = {"msg1": "Valor mensaje - 1", "msg2": "Valor mensaje - 2"}
#     return render(request, "bienvenido.html", mensajes)


def bienvenido(request):
    no_person = Person.objects.count()
    # persons = Person.objects.all()
    persons = Person.objects.order_by("id")
    return render(
        request, "bienvenido.html", {"no_person": no_person, "persons": persons}
    )


# def despedida(request):
#     return HttpResponse("Adios a todos")


# def contacto(resque):
#     return HttpResponse("Celular: 77999469- Email: fercho@gmail.com")

from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from persons.forms import FormPerson
from persons.models import Person


# Create your views here.
def detail_person(request, id):
    # person = Person.objects.get(pk=id)
    person = get_object_or_404(Person, pk=id)
    return render(request, "persons/detail.html", {"person": person})


# PersonForm = modelform_factory(Person, exclude=[])


# def new_person(request):
#     if request.method == "POST":
#         personform = PersonForm(request.POST)
#         if personform.is_valid():
#             personform.save()
#             return redirect("index")
#     else:
#         personform = PersonForm()

#     return render(request, "persons/new_person.html", {"personform": personform})


##Con validacines del servidor
def new_person(request):
    if request.method == "POST":
        personform = FormPerson(request.POST)
        if personform.is_valid():
            personform.save()
            return redirect("index")
    else:
        personform = FormPerson()

    return render(request, "persons/new_person.html", {"personform": personform})

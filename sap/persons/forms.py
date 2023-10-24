from persons.models import Person
from django.forms import ModelForm, EmailInput


class FormPerson(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        # !nos sirve para validaciones desde el servidor
        widgets = {"email": EmailInput(attrs={"type": "email"})}

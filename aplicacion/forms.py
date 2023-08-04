from django import forms

class AutoForm(forms.Form):
    marca = forms.CharField(label="Marca del auto",max_length=50, required=True)
    version = forms.CharField(label="Version", max_length=50, required=True)
    año = forms.IntegerField(label="AÑO", required=True)
    color = forms.CharField(label="color", max_length=50, required=True)
    Kilometros= (
        (1, " "),
        (2, "de 0 a 10.000 kms"),
        (3, "de 10.000 a 50.000 kms"),
        (4, "mas de 50.000 kms"),
    )
    condicion = forms.ChoiceField(label="Condicion", choices=Kilometros, required=True )
    documantacion = forms.BooleanField()


class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cliente", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    mail = forms.EmailField(label="Correo electrónico", required=True)
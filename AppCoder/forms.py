from django import forms


class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class estudianteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    
class profesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesión = forms.CharField()

class entregableFormulario(forms.Form):
    nombre = forms.CharField()
    fechaEntrega = forms.DateField()
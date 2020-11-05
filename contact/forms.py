from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
    attrs={'class':'form-control', 'placeholder':'Juanito Perez'}
  ), max_length=100, min_length=3)
  email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
    attrs={'class':'form-control', 'placeholder':'correo@correo.com'}
  ), max_length=100, min_length=3)
  content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
    attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu menssaje'}
  ), max_length=1000, min_length=10)
from django import forms

class ContactForm(forms.Form):
    sexo = forms.ChoiceField(label="Sexo")
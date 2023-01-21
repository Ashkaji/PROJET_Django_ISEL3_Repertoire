from django import forms

from contact.models import Contact
from django.forms import TextInput


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", 'tel']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Entrez le nom ...', 'class': 'form-control'}),
            'tel': TextInput(attrs={'placeholder': 'Entrez le téléphone ...', 'class': 'form-control'}),
        }

        labels = {"name": "",
                  'tel': ""}

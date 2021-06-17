from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': "Enter your name"})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': "name@example.com"})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'placeholder': "Enter your subject"})
        self.fields['message'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': "Enter your message", 'style': "height: 10rem"}
        )
        self.label_suffix = ''

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Nome',
            'subject': 'Assunto',
            'message': 'Mensagem'
        }

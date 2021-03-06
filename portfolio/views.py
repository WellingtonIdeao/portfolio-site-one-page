from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views.generic.edit import CreateView

# Create your views here.


class Index(CreateView):
    form_class = ContactForm
    template_name = 'portfolio/index.html'
    success_url = reverse_lazy('portfolio:index')

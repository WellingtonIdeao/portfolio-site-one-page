from django.urls import path
from django.views.generic import TemplateView
from .views import Index

app_name = 'portfolio'
urlpatterns = [
    path('', Index.as_view(), name='index'),
]

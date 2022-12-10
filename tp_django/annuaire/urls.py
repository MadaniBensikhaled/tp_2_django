from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<type>particuliers|entreprises)$', views.list, name='list'),
    re_path(r'^contact/(?P<nom>[a-zA-Z ]+)_(?P<prenom>[a-zA-Z ]*)$', views.contact, name='contact'),
]
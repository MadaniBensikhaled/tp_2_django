from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.template_helloWorld, name='template_helloWorld'),

    #Dans l'url, mettre la valeur des deux nombres
    #Exemple : .../sum/sum_page_500_30
    #Va afficher : "La somme est égale à 530."
    path('sum_page_<int:num1>_<int:num2>', views.template_sum, name='template_sum'),

    #Dans l'url, mettre la valeur des deux nombres au format regex
    #Exemple : .../sum/sum_page_regex_2_40007
    #Va afficher : "La somme est égale à 40009."
    re_path(r'^sum_page_regex_(?P<num1>[0-9]+)_(?P<num2>[0-9]+)$', views.template_sum_regex, name='template_sum_regex'),
]
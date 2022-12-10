from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

from datetime import datetime, date

def template_helloWorld(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()
    context = {
        "current_time" : current_time,
        "current_date" : current_date,
    }
    return render(request, 'accueil/helloWorld.html', context)

#On additionne les deux nombres ici, dans le fichier views.py
def template_sum(request, num1, num2):
    sum = num1 + num2
    context = {
        "sum" : sum,
    }
    return render(request, 'sum/sum.html', context)

#On additionne les deux nombres dans le template sum_regex.html
def template_sum_regex(request, num1, num2):
    num1_int = int(num1)
    num2_int = int(num2)
    context = {
        "num1" : num1_int,
        "num2" : num2_int,
    }
    return render(request, 'sum/sum_regex.html', context)
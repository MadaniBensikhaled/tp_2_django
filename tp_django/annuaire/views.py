from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Index de l'application annuaire.")

contacts = [
    {
        "nom": "Cassidy",
        "prenom": "Hammond",
        "telephone": "03 94 96 50 97",
        "entreprise": "0"
    },
    {
        "nom": "Charde",
        "prenom": "Hyde",
        "telephone": "03 44 84 02 60",
        "entreprise": "0"
    },
    {
        "nom": "Dorian",
        "prenom": "Bailey",
        "telephone": "03 78 24 49 97",
        "entreprise": "0"
    },
    {
        "nom": "Vivien",
        "prenom": "Duffy",
        "telephone": "03 26 81 80 44",
        "entreprise": "0"
    },
    {
        "nom": "Ivory",
        "prenom": "Colon",
        "telephone": "03 85 87 65 55",
        "entreprise": "0"
    },
    {
    	"nom": "Mollis Lectus Pede Foundation",
		"prenom": "",
		"telephone": "07 78 07 96 07",
		"entreprise": "1"
	},
	{
		"nom": "Orci LLC",
		"prenom": "",
		"telephone": "03 47 72 76 30",
		"entreprise": "1"
	},
	{
		"nom": "Montes Nascetur Ridiculus Ltd",
		"prenom": "",
		"telephone": "05 75 63 52 48",
		"entreprise": "1"
	},
	{
		"nom": "Volutpat Nulla Consulting",
		"prenom": "",
		"telephone": "09 18 47 42 35",
		"entreprise": "1"
	},
	{
		"nom": "Vitae Company",
		"prenom": "",
		"telephone": "04 28 63 52 29",
		"entreprise": "1"
	}
]


#------ En utilisant les données en local

#def list(request):
#    context = {
#        "contacts" : contacts,
#    }
#    return render(request, 'list.html', context)

#def contact(request, nom, prenom):
#    personne_correspondante = None
#    for personne in contacts:
#        if personne["nom"] == nom and personne["prenom"] == prenom:
#            personne_correspondante = personne
#    context = {
#        "personne" : personne_correspondante,
#    }
#    return render(request, 'contact.html', context)



#------ En utilisant la base de données de Django

#On importe le classe du modèle
from annuaire.models import Contact

#On vide la base de données pour éviter les doublons
Contact.objects.all().delete()

#On injecte les données dans la base de données
for personne in contacts:
    valeur_entreprise = False
    if personne["entreprise"] == "0":
        valeur_entreprise = False
    elif personne["entreprise"] == "1":
        valeur_entreprise = True
    a = Contact(nom = personne["nom"], prenom = personne["prenom"], telephone = personne["telephone"], entreprise = valeur_entreprise)
    a.save()

def list(request, type):
    #On récupère les données de la base de données
    contact_database = Contact.objects.all()
    #On tri pour garder que les particulier
    particuliers = []
    #Pages Blanches
    if type == "particuliers":
        for personne in contact_database:
            if personne.entreprise == False:
                particuliers.append(personne)
    #Page Jaunes
    elif type == "entreprises":
        for personne in contact_database:
            if personne.entreprise == True:
                particuliers.append(personne)
    context = {
        "contacts" : particuliers,
    }
    return render(request, 'list.html', context)

def contact(request, nom, prenom):
    personne_correspondante = None
    #On récupère les données de la base de données
    contact_database = Contact.objects.all()
    for personne in contact_database:
        #Pas le même syntaxe : exemple : personne.nom au lieu de personne["nom"]
        if personne.nom == nom and personne.prenom == prenom:
            personne_correspondante = personne
    context = {
        "personne" : personne_correspondante,
    }
    return render(request, 'contact.html', context)
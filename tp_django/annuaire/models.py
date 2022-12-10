from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50)
    entreprise = models.BooleanField(default=False, blank=False, null=False)
from django.db import models

# Create your models here.

class paire(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    marque = models.CharField(max_length = 100)
    annee = models.DateField(blank=True, null = True) # champs de type date, pouvant être null ou ne pas être rempli
    couleur = models.CharField(max_length=100, blank=False) # champs de type entier devant être obligatoirement rempli
    type = models.CharField(max_length=100, null = True, blank = True) # champs de type text long
    ville = models.ForeignKey("ville", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nom} faite par {self.marque} le {self.annee}."
        return chaine

    def dico(self):
        return {"nom" : self.nom, "marque" : self.marque, "annee" : self.annee, "couleur" : self.couleur, "type" : self.type, "ville" : self.ville }

class ville(models.Model): #déclare la classe Livre héritant de la classe Model, classe de base des modèles
    nom = models.CharField(max_length=100) # défini un champs de type texte de 100 caractères maximum
    quantite = models.CharField(max_length = 100)

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom" : self.nom, "quantite" : self.quantite }

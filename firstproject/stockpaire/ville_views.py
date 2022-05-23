from django.shortcuts import render
from .forms import villeform
from django.http import HttpResponseRedirect
from . import models

# Create your views here.

def traitementv(request):
    form = villeform(request.POST)
    if form.is_valid():
        ville = form.save()
        return HttpResponseRedirect("/stockpaire/")
    else:
        return render(request, "stockpaire/ajoutville.html", {"form": form})

def ajoutpairev(request):
    if request.method == "POST":
        form = villeform(request)
        if form.is_valid():
            ville = form.save()
            return HttpResponseRedirect("/stockpaire/")
        else:
            return render(request, "stockpaire/ajoutville.html", {"form": form})
    else:
        form = villeform()
        return render(request, "stockpaire/ajoutville.html", {"form": form})

def index(request):
    ville = list(models.ville.objects.all())
    return render(request, "stockpaire/index.html", {"liste1":ville})

def afficheville(request, id):
    ville = models.ville.objects.get(pk=id)
    return render(request,"stockpaire/afficheville.html",{"ville" : ville})

def deletev(request, id):
    ville = models.ville.objects.get(pk=id)
    ville.delete()
    return HttpResponseRedirect("/stockpaire/")

def updatev(request, id):
    ville = models.ville.objects.get(pk=id)
    form = villeform(ville.dico())
    return render(request, "stockpaire/updateville.html", {"form": form,"id":id})

def updatepairev(request, id):
    form = villeform(request.POST)
    if form.is_valid():
        ville = form.save(commit=False)
        ville.id = id
        ville.save()
        return HttpResponseRedirect("/stockpaire/")
    else:
        return render(request, "stockpaire/updateville.html", {"form": form, "id": id})


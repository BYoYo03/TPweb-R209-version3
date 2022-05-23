from django.shortcuts import render
from .forms import paireform
from django.http import HttpResponseRedirect
from . import models

# Create your views here.

def traitement(request):
    form = paireform(request.POST)
    if form.is_valid():
        paire = form.save()
        return HttpResponseRedirect("/stockpaire/")
    else:
        return render(request, "stockpaire/ajoutpaire.html", {"form": form})

def ajoutpaire(request):
    if request.method == "POST":
        form = paireform(request)
        if form.is_valid():
            paire = form.save()
            return HttpResponseRedirect("/stockpaire/")
        else:
            return render(request, "stockpaire/ajoutpaire.html", {"form": form})
    else:
        form = paireform()
        return render(request, "stockpaire/ajoutpaire.html", {"form": form})

def home(request):
    paires = list(models.paire.objects.all())

    return render(request, "stockpaire/index.html", {"liste":paires})

def affiche(request, id):
    paire = models.paire.objects.get(pk=id)
    return render(request,"stockpaire/affichepaire.html",{"paire" : paire})

def delete(request, id):
    paire = models.paire.objects.get(pk=id)
    paire.delete()
    return HttpResponseRedirect("/stockpaire/")

def update(request, id):
    paire = models.paire.objects.get(pk=id)
    form = paireform(paire.dico())
    return render(request, "stockpaire/update.html", {"form": form,"id":id})

def updatepaire(request, id):
    form = paireform(request.POST)
    if form.is_valid():
        paire = form.save(commit=False)
        paire.id = id
        paire.save()
        return HttpResponseRedirect("/stockpaire/")
    else:
        return render(request, "stockpaire/update.html", {"form": form, "id": id})


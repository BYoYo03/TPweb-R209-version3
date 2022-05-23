from django.urls import path
from . import views, ville_views

urlpatterns = [
    path('traitement/',views.traitement),
    path('',views.home),
    path('home/',views.home),
    path('ajoutpaire/',views.ajoutpaire),
    path("affiche/<int:id>/",views.affiche),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("updatepaire/<int:id>",views.updatepaire),
    #
    path('',ville_views.index),
    path('traitementv/',ville_views.traitementv),
    path('ajoutpairev/',ville_views.ajoutpairev),
    path("afficheville/<int:id>/",ville_views.afficheville),
    path("deletev/<int:id>",ville_views.deletev),
    path("updateville/<int:id>",ville_views.updatev),
    path("updatepaireville/<int:id>",ville_views.updatepairev),
]
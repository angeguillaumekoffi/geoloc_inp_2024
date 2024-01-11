from django.shortcuts import render
from django.http.response import JsonResponse
from sig.models import Vehicule, Historique
from django.contrib.gis.geos import Point
from json import dumps

def index(request):
    data = {}
    return render(request, 'index.html', data)


def location(request, **kwargs):
    matricule = kwargs.get('matricule', '5201AF')
    vehicule = Vehicule.objects.get(immatriculation=matricule)
    data = {
        'immatriculation': vehicule.immatriculation,
        'marque': vehicule.marque,
        'couleur': vehicule.couleur,
        'longitude' : vehicule.longitude,
        'latitude' : vehicule.latitude
        }
    return JsonResponse(dumps(data), safe=False) 

def send_location(request, **kwargs):
    matricule = kwargs.get('matricule')
    latitude = float(kwargs.get('latitude'))
    longitude = float(kwargs.get('longitude'))

    try:
        # enregiostrement vehicule*
        vehicule = Vehicule.objects.get(immatriculation=matricule)
        vehicule.position = Point(latitude, longitude)
        vehicule.save(update_fields=["position"])

        # Creation de l'historique
        historique = Historique()
        historique.id = Historique.objects.last().id + 1
        historique.vehicule = vehicule.immatriculation
        historique.position = vehicule.position
        historique.save()
        reponse = {"statut": "succes"}
    except Exception as err:
        print(err)
        reponse = {"statut": "error"}
    return JsonResponse(dumps(reponse), safe=False)
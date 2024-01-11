from django.contrib.gis.db import models
from datetime import datetime

class Vehicule(models.Model):
    immatriculation = models.CharField(verbose_name="immatriculation", primary_key=True, unique=True, max_length=20)
    marque = models.CharField(max_length=100)
    couleur = models.CharField(max_length=50)
    modele = models.CharField(verbose_name='modele', max_length=100)
    position = models.PointField(null=True, srid=4326)

    class Meta:
        managed = False
        db_table = 'vehicule'
    
    @property
    def longitude(self):
        return self.position.x
    
    @property
    def latitude(self):
        return self.position.y

class Historique(models.Model):
    id = models.IntegerField(primary_key=True, default=None, blank=True)
    vehicule = models.CharField(max_length=20)
    position = models.PointField(srid=4326)
    date_heure = models.DateTimeField(default=datetime.now())

    class Meta:
        managed = False
        db_table = 'historique'

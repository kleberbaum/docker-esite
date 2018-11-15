# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid

# Create your models here.

class Messdaten(models.Model):
    UID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Temperatur= models.FloatField()
    Luftdruck= models.FloatField()
    Luftfeuchtigkeit = models.FloatField()
    VOC = models.FloatField()
    FEINSTAUBPM25 = models.FloatField()
    FEINSTAUBPM100 = models.FloatField()
    Datum = models.DateField()
    DatumZeit = models.DateTimeField()

    def __str__(self):

        return self.title

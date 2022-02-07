from django.db import models
from django.utils import timezone


# import datetime
# print(datetime.__file__)

# Create your models here.
# DataFlair Models


class Hadir(models.Model):
    nip = models.CharField(max_length=50)
    mac = models.CharField(max_length=50, default="34:97:F6:75:A1:AF")
    nama = models.CharField(max_length=50)
    lat = models.CharField(max_length=50, default="-6.245284601263033")
    # lat = models.CharField(max_length=50, default='-6.173799991607666')ASLI

    city = models.CharField(max_length=50, default="Jakarta")
    lng = models.CharField(max_length=50, default="106.86886090646962")
    # lng = models.CharField(max_length=50, default='106.82669830322266')ASLI

    # tgl = models.CharField(max_length=50, default='Aug. 16, 2021')
    # time = models.CharField(max_length=50, default='4:12 p.m')
    waktu = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.nama

# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
import geoip2.database

# import requests
from .models import Hadir
from .forms import HadirCreate
from django.http import HttpResponse
from uuid import getnode as get_mac
from ipstack import GeoLookup
import requests
import json
import datetime
from django.contrib import messages


def index(request):
    shelf = Hadir.objects.order_by("-waktu")
    # lokasi = print(response.city.name)
    time = datetime.datetime.now().time()
    tgl = datetime.date.today()
    return render(
        request,
        "hadir/listkehadiran.html",
        {"shelf": shelf, "time": time, "tgl": tgl},
    )

    # response = requests.get('https://api.kawalcorona.com/indonesia/')
    # corona = response.json()
    # return render(request, 'hadir/listkehadiran.html', {
    #     'name': corona['name'],
    #     'positif': geodata['positif']
    # })


def render_to_json(request, data):
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
        mimetype=request.is_ajax() and "application/json" or "text/html",
    )


def upload(request):

    # geolocator = Nominatim(user_agent='hadir')
    form = HadirCreate(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Data Presensi Berhasil Masuk"),
        return redirect("index")
    else:
        # ip = request.META.get('REMOTE_ADDR')
        geo_lookup = GeoLookup("b85c1f45d890a23b659a1fe1c953a373")
        lokasi = geo_lookup.get_own_location()
        mac2 = get_mac()
        mac = ":".join(("%012X" % mac2)[i : i + 2] for i in range(0, 12, 2))
        # lat = lokasi["latitude"]
        # lng = lokasi["longitude"]
        city = lokasi["city"]
        time = datetime.datetime.now().time()
        tgl = datetime.date.today()

        return render(
            request,
            "hadir/upload_form.html",
            {
                "upload_form": HadirCreate,
                "city": city,
                "time": time,
                "tgl": tgl,
                # "lat": lat,
                # "lng": lng,
                "mac": mac,
            },
        )


def update_hadir(request, hadir_id):
    hadir_id = int(hadir_id)
    try:
        hadir_sel = Hadir.objects.get(id=hadir_id)
    except Hadir.DoesNotExist:
        return redirect("index")
    hadir_form = HadirCreate(request.POST or None, instance=hadir_sel)
    if hadir_form.is_valid():
        hadir_form.save()
        return redirect("index")
    return render(request, "hadir/upload_form.html", {"upload_form": hadir_form})


def delete_hadir(request, hadir_id):
    hadir_id = int(_id)
    try:
        hadir_sel = Hadir.objects.get(id=hadir_id)
    except Hadir.DoesNotExist:
        return redirect("index")
    hadir_sel.delete()
    return redirect("index")

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV

DATA = []
with open(BUS_STATION_CSV, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for i in reader:
        DATA.append({'Name': i['Name'], 'Street': i['Street'], 'District': i['District']})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(DATA, 10)
    page = paginator.page(page_number)
    print(page)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context=context)

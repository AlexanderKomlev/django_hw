from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open(f'{BUS_STATION_CSV}', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    station_list = []
    for row in reader:
        station_list.append(row)


def bus_stations(request):

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(station_list, 7)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

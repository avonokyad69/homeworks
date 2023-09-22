from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import pandas as pd
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    path = settings.BUS_STATION_CSV
    data = pd.read_csv(path, usecols=['Name', 'Street', 'District'])
    print(data)
    bus_stations = data.to_dict(orient='records')
    paginator = Paginator(bus_stations, 100)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import UtilityForm
from .models import Pumps, Lights, FlowMeter
from django.contrib import messages

import pandas as ps
import plotly.express as px
from plotly.offline import plot
from django.views.generic.base import TemplateView

import numpy
from numpy import mean
from django.db.models import Avg, Max, Min, Sum


def IndexView(request):
    return render(request, "home/main2.html")


def CostcalView(request):
    # if this is a POST request process the form data
    global form
    price = 10.00
    form = UtilityForm()
    if request.method == 'POST':
        val_1 = request.POST['equipment_name']
        val_2 = request.POST['quantity']
        val_3 = request.POST['rating']
        val_4 = request.POST['hours_used']
        val_5 = request.POST['date']

        if val_1 == 'Pumps':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Pumps(date=val_5, hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Lights':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Lights(date=val_5, hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Flow Meter':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = FlowMeter(date=val_5, hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()


        else:
            messages.success(request, 'error')

        # redirect to a new URL:
        # return HttpResponse('thanks')
        messages.success(request, 'Successfully added, for more entries click the add button...')

    # if a GET (or any other method) create a blank form
    else:
        form = UtilityForm()
    return render(request, 'home/costcal.html', {'form': form})


class LightConsumption(TemplateView):
    template_name = 'light.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Lights.objects.filter(date__istartswith='2022-02').values_list('consumption', flat=True)


        fig = px.bar(x=x, y=y,
                     labels={
                         "x": "February",
                         "y": "Consumption (kWh)",
                     })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


class PumpConsumption(TemplateView):
    template_name = 'pump.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ['Week1', 'Week2', 'Week3', 'Week4']
        y = Pumps.objects.filter(date__istartswith='2022-02').values_list('consumption', flat=True)

        fig = px.bar(x=x, y=y,
                     labels={
                         "x": "February",
                         "y": "Consumption (kWh)",
                     })
        div = plot(fig, auto_open=False, output_type='div')
        context['graph'] = div
        return context


def Ebc(request):
    pump = Pumps.objects.all()
    light = Lights.objects.all()

    total_pump_c = Pumps.objects.values_list('consumption', flat=True).aggregate(sum=Sum('consumption'))['sum']
    total_light_c = Lights.objects.values_list('consumption', flat=True).aggregate(sum=Sum('consumption'))['sum']

    pump_total_cost = Pumps.objects.values_list('daily_cost', flat=True).aggregate(sum=Sum('daily_cost'))['sum']
    lights_total_cost = Lights.objects.values_list('daily_cost', flat=True).aggregate(sum=Sum('daily_cost'))['sum']

    return render(request, 'home/ebc.html', {'pump': pump,
                                             'light': light,
                                             'total_pump_c': total_pump_c,
                                             'total_light_c': total_light_c,
                                             'pump_total_cost': pump_total_cost,
                                             'lights_total_cost': lights_total_cost,
                                             })



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

        if val_1 == 'Pumps':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Pumps(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Lights':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = Lights(hours_used=val_4, daily_cost=cost, consumption=cons)
            ins.save()

        elif val_1 == 'Flow Meter':
            cost = float(val_4) * float(val_3) * price * float(val_2)
            cons = float(val_4) * float(val_3) * float(val_2)
            ins = FlowMeter(hours_used=val_4, daily_cost=cost, consumption=cons)
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





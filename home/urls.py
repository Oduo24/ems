
from django.urls import path
from . import views
from .views import IndexView, CostcalView, LightConsumption, PumpConsumption, Ebc


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('index/', views.IndexView, name='index'),
    path('index/utility/entry', views.CostcalView, name="costcal"),
    path('index/analytics/001L', LightConsumption.as_view(), name='LightConsumption'),
    path('index/analytics/002P', PumpConsumption.as_view(), name='PumpConsumption'),
    path('index/ebc/000c', views.Ebc, name='ebc'),






]











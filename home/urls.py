
from django.urls import path
from . import views
from .views import IndexView, CostcalView, Ebc, JanLightConsumption, JanPumpConsumption, FebLightConsumption, FebPumpConsumption, MarchLightConsumption, MarchPumpConsumption, AprilLightConsumption, AprilPumpConsumption, MayLightConsumption, MayPumpConsumption, JuneLightConsumption, JunePumpConsumption, JulyLightConsumption, JulyPumpConsumption, AugLightConsumption, AugPumpConsumption, SepLightConsumption, SepPumpConsumption, OctLightConsumption, OctPumpConsumption, NovLightConsumption, NovPumpConsumption, DecLightConsumption, DecPumpConsumption


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('index/', views.IndexView, name='index'),
    path('index/utility/entry', views.CostcalView, name="costcal"),
    path('index/analytics/01L', JanLightConsumption.as_view(), name='JanLightConsumption'),
    path('index/analytics/01P', JanPumpConsumption.as_view(), name='JanPumpConsumption'),

    path('index/analytics/02L', FebLightConsumption.as_view(), name='FebLightConsumption'),
    path('index/analytics/02P', FebPumpConsumption.as_view(), name='FebPumpConsumption'),

    path('index/analytics/03L', MarchLightConsumption.as_view(), name='MarchLightConsumption'),
    path('index/analytics/03P', MarchPumpConsumption.as_view(), name='MarchPumpConsumption'),

    path('index/analytics/04L', AprilLightConsumption.as_view(), name='AprilLightConsumption'),
    path('index/analytics/04P', AprilPumpConsumption.as_view(), name='AprilPumpConsumption'),

    path('index/analytics/05L', MayLightConsumption.as_view(), name='MayLightConsumption'),
    path('index/analytics/05P', MayPumpConsumption.as_view(), name='MayPumpConsumption'),

    path('index/analytics/06L', JuneLightConsumption.as_view(), name='JuneLightConsumption'),
    path('index/analytics/06P', JunePumpConsumption.as_view(), name='JunePumpConsumption'),

    path('index/analytics/07L', JulyLightConsumption.as_view(), name='JulyLightConsumption'),
    path('index/analytics/07P', JulyPumpConsumption.as_view(), name='JulyPumpConsumption'),

    path('index/analytics/08L', AugLightConsumption.as_view(), name='AugLightConsumption'),
    path('index/analytics/08P', AugPumpConsumption.as_view(), name='AugPumpConsumption'),

    path('index/analytics/09L', SepLightConsumption.as_view(), name='SepLightConsumption'),
    path('index/analytics/09P', SepPumpConsumption.as_view(), name='SepPumpConsumption'),

    path('index/analytics/10L', OctLightConsumption.as_view(), name='OctLightConsumption'),
    path('index/analytics/10P', OctPumpConsumption.as_view(), name='OctPumpConsumption'),

    path('index/analytics/11L', NovLightConsumption.as_view(), name='NovLightConsumption'),
    path('index/analytics/11P', NovPumpConsumption.as_view(), name='NovPumpConsumption'),

    path('index/analytics/12L', DecLightConsumption.as_view(), name='DecLightConsumption'),
    path('index/analytics/12P', DecPumpConsumption.as_view(), name='DecPumpConsumption'),


    path('index/ebc/000c', views.Ebc, name='ebc'),
    path('index/est/0000', views.EnergySavingTips, name='EnergySavingTips'),






]












from django.urls import path
from . import views
from .views import IndexView, CostcalView


urlpatterns = [
    path('', views.IndexView, name='index'),
    path('index/', views.IndexView, name='index'),
    path('index/costcal', views.CostcalView, name="costcal"),






]











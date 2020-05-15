from django.urls import path
from django.conf.urls import include
from bouquetapp import views
from .views import *

app_name = "bouquetapp"

urlpatterns = [
    path('', home, name='home'),
    path('bouquetform/', create_bouquet_form, name='create_bouquet_form'),
]

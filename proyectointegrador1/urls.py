from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from measure import views as measure_views

urlpatterns = [
    path('', measure_views.measure, name='measure'),
]


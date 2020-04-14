from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from measure import views

router = routers.DefaultRouter()
router.register(r'temphum', views.MeasureViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]


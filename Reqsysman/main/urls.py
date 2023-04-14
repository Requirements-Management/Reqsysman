from django.urls import path, include
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import RequirementViewSet

router = routers.DefaultRouter()
router.register(r'requirements', RequirementViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('Reqsysman', views.Reqsysman),
    path('Reqsysman', views.index),
    path('github', views.github)
]
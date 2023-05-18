from django.urls import path, include
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import RequirementViewSet

router = routers.DefaultRouter()
router.register(r'requirements', RequirementViewSet)


urlpatterns = [
    path('', views.index),
    path('Reqsysman/', views.Reqsysman),
    path('Reqsysman/', include(router.urls)),
    path('github/', views.github)
]
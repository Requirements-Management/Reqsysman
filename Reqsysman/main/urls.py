from django.urls import path, include
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import RequirementViewSet
from django.contrib import admin
from .views import requirements_list

router = routers.DefaultRouter()
router.register(r'requirements', RequirementViewSet)
app_name = 'main'

urlpatterns = [
    path('', views.index),

    path('admin/', admin.site.urls),
    #path('add/', views.add_requirement, name='add_requirement'),
    path('Reqsysman/', views.requirements_list, name='requirements_list'),

#    path('Reqsysman/add/', views.add_requirement, name='add_requirement'),
    path('', views.requirements_list, name='requirements_list'),
    #path('Reqsysman/', views.Reqsysman),
    #path('Reqsysman/', requirements_list, name='requirements_list'),
    #path('Reqsysman/', include(router.urls)),
    path('github/', views.github),

    path('Reqsysman/', views.Reqsysman),
    path('Reqsysman/', include(router.urls)),
    path('github/', views.github)
]

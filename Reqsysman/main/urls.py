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
    path('github/', views.github),
    path('Reqsysman/', views.requirements),
    path('new_requirement/', views.new_requirement),
    path('accounts/', include('allauth.urls')),
    path('repository/files/', views.display_repository_files, name='repository_files'),


    # path('', view.index),

    # path('Reqsysman/', views.requirements_list, name='requirements_list'),
    # path('Reqsysman/', views.Reqsysman),
    # path('Reqsysman/', include(router.urls)),

    # commented
    #path('add/', views.add_requirement, name='add_requirement'),
    #path('Reqsysman/add/', views.add_requirement, name='add_requirement'),
    #path('Reqsysman/', views.Reqsysman),
    #path('Reqsysman/', requirements_list, name='requirements_list'),
    #path('Reqsysman/', include(router.urls)),
]

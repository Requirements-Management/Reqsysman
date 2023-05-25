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
from allauth.account import views as account_views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('github/', views.github),
    path('accounts/', include('allauth.urls')),
    path('repository/files/', views.display_repository_files, name='repository_files'),
    path('Reqsysman/', views.RequirementView.requirements, name='requirements'),
    path('new_requirement/', views.RequirementView.new_requirement, name='new_requirement'),
    path('test/', views.test, name='test'),
    # path('accounts/github/login/', views.github_login, name='github_login'),
    # path('accounts/social/login/', account_views.LoginView.as_view(), name='socialaccount_login'),
    
    


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

"""
URL configuration for unhabitat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from projects import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
        path('create/', views.ProjectCreateView.as_view(), name='project_create'),
            path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='project_update'),
                path('delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='project_delete'),
                    path('projects/', views.ProjectListView.as_view(), name='project_list'),
                        path('dashboard/', views.dashboard_view, name='dashboard'),
                            path('', include('projects.urls')),

                        ]

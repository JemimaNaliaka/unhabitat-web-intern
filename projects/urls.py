from django.urls import path
from . import views
from .views import project_detail
from .views import project_list_api
from .views import ProjectUpdateView


urlpatterns = [
    path('', views.home, name='home'),
        path('create/', views.project_create, name='project_create'),
            path('<int:pk>/', views.project_detail, name='project_detail'),
                path('<int:pk>/edit/', views.project_update, name='project_update'),
                    path('<int:pk>/delete/', views.project_delete, name='project_delete'),
                        #path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
                            #path('api/projects/', project_api, name='project-api'),
                        #path('api/projects/', project_list_api, name='project_list_api'),
                        path('projects/', views.project_list_api, name='project_list_api'),
                        path('projects/<int:pk>/', project_detail, name='project_detail'),
                        path('update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
                            ]


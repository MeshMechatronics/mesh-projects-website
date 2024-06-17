"""
URL configuration for mesh_project_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from main import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('', views.index, name='index'),
#     path('materials/', views.materials, name='materials'),
#     path('create-quote/', views.create_quote, name='create_quote'),
#     path('projects/', views.view_projects, name='projects'),  # Yeni eklenen
#     path('create-company/', views.create_company, name='create_company'),
#     path('create-project/', views.create_project, name='create_project'),
#     path('companies/', views.view_companies, name='view_companies'),
#     path('projects/<int:company_id>/', views.view_projects, name='view_projects'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('materials/', views.materials, name='materials'),
    path('create-quote/', views.create_quote, name='create_quote'),
    path('projects/', views.projects, name='projects'),
    path('create-company/', views.create_company, name='create_company'),
    path('create-project/', views.create_project, name='create_project'),
    path('companies/', views.view_companies, name='view_companies'),
    path('projects/<int:company_id>/', views.company_projects, name='company_projects'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:company_id>/', views.company_projects, name='company_projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
]

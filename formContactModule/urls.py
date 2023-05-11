"""
URL configuration for formContact project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib                             import admin
from django.urls                                import path, include
from formContactApp                             import views
from formContactApp.models.form                 import Form
from formContactApp.views.formView              import FormView
from formContactApp.views.formFilteredView      import FormFilteredView
from formContactApp.views.formCreateView        import FormCreateView
from formContactApp.views.formDeleteView        import FormDeleteView
from formContactApp.views.formUpdateView        import FormUpdateView


urlpatterns = [
    #URL´s del formulario
    path('form/all/', views.FormView.as_view()), #ver todos los productos
    path('form/filtered/<int:pk>/', views.FormFilteredView.as_view()), #ver productos filtrados
    path('form/create/', views.FormCreateView.as_view()), #crear un producto
    path('form/delete/<int:pk>/', views.FormDeleteView.as_view()), #borrar un producto
    path('form/update/<int:pk>/', views.FormUpdateView.as_view()), #actualizar un producto
]

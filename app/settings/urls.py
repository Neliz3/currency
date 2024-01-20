"""
URL configuration for settings project.

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
# from django.contrib import admin
from django.urls import path

from currency_app.views import hello_world, get_data, get_row, get_source, get_source_by_id

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('get_data/', get_data),
    path('get_row/<int:pk>/', get_row),
    path('show_banks/', get_source),
    path('show_banks/<int:pk>/', get_source_by_id),
]

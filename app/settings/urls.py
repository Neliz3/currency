from django.contrib import admin
from django.urls import path

#from currency_app.views import generate_address
from currency_app.views import get_text

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('gen-address/', generate_address),
    path('get_text/', get_text),
]

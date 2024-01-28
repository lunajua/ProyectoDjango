
from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, segunda_vista #Accedo a la vista del módulo y del método importando los mismos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    
]
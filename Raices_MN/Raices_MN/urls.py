from django.contrib import admin
from django.urls import path

from Raices_MN.views import homeMetodo, pregunta_crear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeMetodo/', homeMetodo),  #Regitrar prueba de vista
    path('pregunta/', pregunta_crear),
  
]

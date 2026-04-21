from django.urls import path
from company_structure.views import *

urlpatterns = [
    path("", home, name="home"),
    path("company_structure/", departamentos_list, name="departamentos_list"),
    path("company_structure/<int:nro_departamento>/", ver_departamento, name="departamento_detail"),
    path("company_structure/crear/", crear_departamento, name="departamento_create"),
]
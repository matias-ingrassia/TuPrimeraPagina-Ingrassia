from django.urls import path
from company_structure.views import *

urlpatterns = [
    path("", home, name="home"),
    path("company_structure/", area_list, name="area_list"),
    path("company_structure/<int:nro_departamento>/", area_detail, name="area_detail"),
    path("company_structure/create/", area_new, name="area_create"),
]
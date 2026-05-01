from django.urls import path
from company_structure.views import *

urlpatterns = [
    path("", home, name="home"),
    path("area/", area_list, name="area_list"),
    path("area/<int:area_id>/", area_detail, name="area_detail"),
    path("area/new/", area_new, name="area_new"),

    path("department/", department_list, name="department_list"),
    path("department/<int:department_id>/", department_detail, name="department_detail"),
    path("department/new/", department_new, name="department_new"),

    path("team/", team_list, name="team_list"),
    path("team/<int:team_id>/", team_detail, name="team_detail"),
    path("team/new/", team_new, name="team_new"),

    path("employee/", employee_list, name="employee_list"),
    path("employee/<int:employee_id>/", employee_detail, name="employee_detail"),
    path("employee/new/", employee_new, name="employee_new"),

    path("role/", role_list, name="role_list"),
    path("role/<int:role_id>/", role_detail, name="role_detail"),
    path("role/new/", role_new, name="role_new"),
]
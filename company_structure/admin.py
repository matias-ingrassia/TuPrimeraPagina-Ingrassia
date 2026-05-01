from django.contrib import admin
from company_structure.models import AreaModel, DepartmentModel, TeamModel, EmployeeModel, RoleModel

@admin.register(AreaModel)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("area_id", "name", "lead")
    list_display_links = ("name",)
    search_fields = ("area_id", "name", "lead",)
    list_filter = ("creation_date",)
    ordering = ("area_id",)
    readonly_fields = ("creation_date",)

@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_id", "name", "lead", "area",)
    list_display_links = ("name",)
    search_fields = ("department_id", "name", "lead", "area",)
    list_filter = ("creation_date",)
    ordering = ("department_id",)
    readonly_fields = ("creation_date",)

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_id", "name", "lead", "department",)
    list_display_links = ("name",)
    search_fields = ("team_id", "name","department",)
    list_filter = ("creation_date",)
    ordering = ("team_id",)
    readonly_fields = ("creation_date",)

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "name", "role", "email", "phone_number", "mobile_number", "team",)
    list_display_links = ("name",)
    search_fields = ("employee_id", "name", "team",)
    list_filter = ("creation_date",)
    ordering = ("employee_id",)
    readonly_fields = ("creation_date",)

@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_id", "name", "description",)
    list_display_links = ("name",)
    search_fields = ("role_id", "name", "description",)
    list_filter = ("creation_date",)
    ordering = ("role_id",)
    readonly_fields = ("creation_date",)
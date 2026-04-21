from django.contrib import admin
from company_structure.models import AreaModel, DepartmentModel, TeamModel, EmployeeModel, RoleModel

@admin.register(AreaModel)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "lead")
    list_display_links = ("name",)
    search_fields = ("id", "name")
    list_filter = ("creation_date",)
    ordering = ("name")
    readonly_fields = ("creation_date",)

@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "area", "lead")
    list_display_links = ("name",)
    search_fields = ("id", "name")
    list_filter = ("creation_date", "area")
    ordering = ("name")
    readonly_fields = ("creation_date",)

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "department", "lead")
    list_display_links = ("name",)
    search_fields = ("id", "name")
    list_filter = ("creation_date", "department")
    ordering = ("name")
    readonly_fields = ("creation_date",)

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "role", "email", "phone", "mobile", "team")
    list_display_links = ("name",)
    search_fields = ("id", "name", "surname")
    list_filter = ("creation_date", "role")
    ordering = ("name")
    readonly_fields = ("creation_date",)

@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)
    search_fields = ("id", "name")
    ordering = ("name",)
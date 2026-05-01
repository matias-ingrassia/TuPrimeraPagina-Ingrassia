from django.shortcuts import render, get_object_or_404, redirect
from company_structure.models import AreaModel, DepartmentModel, TeamModel, EmployeeModel, RoleModel
from company_structure.forms import AreaForm, DepartmentForm, TeamForm, EmployeeForm, RoleForm
from django.http import Http404

def home(request):
    return render(request, "company_structure/index.html")

# -------------------------------------------------------------------------------------------------------
# AREA VIEWS
def area_list(request):
    name = request.GET.get("name")
    area_query = AreaModel.objects.all()
    if name is not None:
        area_query = AreaModel.objects.filter(
            name__icontains=name
        )
    context = {
        "area_list": list(area_query)
    }

    return render(request, "company_structure/area_list.html", context)

def area_detail(request, area_id):
    area = AreaModel.objects.get(area_id=area_id)
    area2 = get_object_or_404(AreaModel, area_id=area_id)
    context = {
        "area_q" : area
    }
    
    return render(request, "company_structure/area_detail.html", context)

def area_new(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("area_list")
    else:
        form = AreaForm()
    
    return render(request, "company_structure/area_new.html", {"form": form})

# -------------------------------------------------------------------------------------------------------
# DEPARTMENT VIEWS
def department_list(request):
    name = request.GET.get("name")
    department_query = DepartmentModel.objects.all()
    if name is not None:
        department_query = DepartmentModel.objects.filter(
            name__icontains=name
        )
    context = {
        "department_list": list(department_query)
    }

    return render(request, "company_structure/department_list.html", context)

def department_detail(request, department_id):
    department = DepartmentModel.objects.get(department_id=department_id)
    department2 = get_object_or_404(DepartmentModel, department_id=department_id)
    context = {
        "department_q" : department
    }
    
    return render(request, "company_structure/department_detail.html", context)

def department_new(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm()
    
    return render(request, "company_structure/department_new.html", {"form": form})

# -------------------------------------------------------------------------------------------------------
# TEAM VIEWS
def team_list(request):
    name = request.GET.get("name")
    team_query = TeamModel.objects.all()
    if name is not None:
        team_query = TeamModel.objects.filter(
            name__icontains=name
        )
    context = {
        "team_list": list(team_query)
    }

    return render(request, "company_structure/team_list.html", context)

def team_detail(request, team_id):
    team = TeamModel.objects.get(team_id=team_id)
    team2 = get_object_or_404(TeamModel, team_id=team_id)
    context = {
        "team_q" : team
    }
    
    return render(request, "company_structure/team_detail.html", context)

def team_new(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("team_list")
    else:
        form = TeamForm()
    
    return render(request, "company_structure/team_new.html", {"form": form})

# -------------------------------------------------------------------------------------------------------
# EMPLOYEE VIEWS
def employee_list(request):
    name = request.GET.get("name")
    employee_query = EmployeeModel.objects.all()
    if name is not None:
        employee_query = EmployeeModel.objects.filter(
            name__icontains=name
        )
    context = {
        "employee_list": list(employee_query)
    }

    return render(request, "company_structure/employee_list.html", context)

def employee_detail(request, employee_id):
    employee = EmployeeModel.objects.get(employee_id=employee_id)
    employee2 = get_object_or_404(EmployeeModel, employee_id=employee_id)
    context = {
        "employee_q" : employee
    }
    
    return render(request, "company_structure/employee_detail.html", context)

def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    
    return render(request, "company_structure/employee_new.html", {"form": form})

# -------------------------------------------------------------------------------------------------------
# ROLE VIEWS
def role_list(request):
    name = request.GET.get("name")
    role_query = RoleModel.objects.all()
    if name is not None:
        role_query = RoleModel.objects.filter(
            name__icontains=name
        )
    context = {
        "role_list": list(role_query)
    }

    return render(request, "company_structure/role_list.html", context)

def role_detail(request, role_id):
    role = RoleModel.objects.get(role_id=role_id)
    role2 = get_object_or_404(RoleModel, role_id=role_id)
    context = {
        "role_q" : role
    }
    
    return render(request, "company_structure/role_detail.html", context)

def role_new(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("role_list")
    else:
        form = RoleForm()
    
    return render(request, "company_structure/role_new.html", {"form": form})
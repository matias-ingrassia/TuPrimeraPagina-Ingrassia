from django.shortcuts import render, get_object_or_404, redirect
from company_structure.models import AreaModel, DepartmentModel, TeamModel, EmployeeModel, RoleModel
from company_structure.forms import AreaForm, DepartmentForm, TeamForm, EmployeeForm, RoleForm
from django.http import Http404


def home(request):
    return render(request, "company_structure/index.html")

# AREAS
def area_list(request):
    name = request.GET.get("name")
    area_query = AreaModel.objects.all()
    if name is not None:
        area_query = AreaModel.objects.filter(
            nombre__icontains=name
        )
    context = {
        "area_list": list(area_query)
    }
    
    return render(request, "company_structure/area_list.html", context)

def area_detail(request, id):
    area = AreaModel.objects.get(id=id)
    area_404 = get_object_or_404(AreaModel, id=id)
    context = {
        "area_query" : area
    }
    
    return render(request, "area/area_detail.html", context)

def area_new(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("area_list")
    else:
        form = AreaForm()
    
    return render(request, "area/area_new.html", {"form": form})
from django.shortcuts import render, get_object_or_404, redirect
from company_structure.models import AreaModel
from company_structure.forms import AreaForm
from django.http import Http404

def home(request):
    return render(request, "company_structure/index.html")


def area_list(request):
    name = request.GET.get("name")
    areas_query = AreaModel.objects.all()  # QuerySet([Cardio, Traumato, ...])
    if name is not None:
        areas_query = AreaModel.objects.filter(
            nombre__icontains=name
        )
    contexto = {
        "area_list": list(areas_query)
    }
    
    return render(request, "company_structure/area_list.html", contexto)


def ver_departamento(request, nro_departamento):

    departamento = AreaModel.objects.get(nro_departamento=nro_departamento)
    departamento2 = get_object_or_404(AreaModel, nro_departamento=nro_departamento)
    contexto = {
        "departamento_q" : departamento
    }
    
    return render(request, "company_structure/departamento_detail.html", contexto)

# GET - Pedir informacion
# POST - Crear/Editar Informacion
# PUT - Actualizar informacion
# DELETE - Eliminar informacion
# ...

def crear_departamento(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departamentos_list")
    else:
        form = AreaForm()
    
    return render(request, "company_structure/depatarmento_create.html", {"form": form})
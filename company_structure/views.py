from django.shortcuts import render, get_object_or_404, redirect
from company_structure.models import DepartamentosMedicos
from company_structure.forms import DepartamentoMedicoForm
from django.http import Http404

def home(request):
    return render(request, "company_structure/index.html")


def departamentos_list(request):
    nombre = request.GET.get("nombre")
    departamentos_query = DepartamentosMedicos.objects.all()  # QuerySet([Cardio, Traumato, ...])
    if nombre is not None:
        departamentos_query = DepartamentosMedicos.objects.filter(
            nombre__icontains=nombre
        )
    contexto = {
        "departamentos_list": list(departamentos_query)
    }
    
    return render(request, "company_structure/departamentos_list.html", contexto)


def ver_departamento(request, nro_departamento):

    departamento = DepartamentosMedicos.objects.get(nro_departamento=nro_departamento)
    departamento2 = get_object_or_404(DepartamentosMedicos, nro_departamento=nro_departamento)
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
        form = DepartamentoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departamentos_list")
    else:
        form = DepartamentoMedicoForm()
    
    return render(request, "company_structure/depatarmento_create.html", {"form": form})
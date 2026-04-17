from django.shortcuts import render

# Create your views here.
def index (request):
    context = {"mensaje": "Bienvenidos a mi aplicacion"}
    return render(request, "sectores/index.html", context)
# TuPrimeraPagina-Ingrassia

## Informacion General
Comision: 89730
Alumno: Matias Ingrassia
DJango: 6.0.4

## Descripcion del proyecto
Tercera entrega de mi courso de Python en Coderhouse. La tematica es un sistema para una fabrica.

## Conocimientos aplicados
- Uso de propiedades en las clases de los modelos para calcular el numero de empleados (models.py)
- Uso de ForeignKeys. Si bien ya conocia el concepto de este tipo de campos en bases de datos, tuve que investigarlo para poder aplicarlo en Django. ([text](https://docs.djangoproject.com/en/6.0/topics/db/models/)) y [text](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey)

## Modo de uso
El proceso está pensado para ingresar areas -> departments -> teams -> roles -> employees.
Luego habrá que editar cada uno (excepto roles) para ir asignando sus dependencias. 
Por ejemplo, role al employee. lead al area... y asi.


# TuPrimeraPagina-Ingrassia

## Informacion General
- Comision: 89730
- Alumno: Matias Ingrassia
- DJango: 6.0.4

## Descripcion del proyecto
Tercera entrega de mi courso de Python en Coderhouse. La temática es un sistema administrativo para una fábrica.

## Modo de uso
El proceso está pensado para ingresar areas -> departments -> -> teams -> roles -> employees.
Luego habrá que editar cada uno (excepto roles) para ir asignando sus dependencias. 
Por ejemplo, role al employee. lead al area... y asi.

## Comentarios
Estuve investigando el uso de ForeignKeys (branch dev). Si bien ya conocia el concepto de este tipo de campos en bases de datos, tuve que investigarlo para poder aplicarlo en Django. Creando dependencias de campos (employee_id -> team_id -> department_id -> area_id) esto permitiria el calculo de cantidad de empleados como una propiedad de cada clase. Sin embargo, lo dejé de lado por los problemas que encontré en la visualizacion del sitio, que no pude resolver.
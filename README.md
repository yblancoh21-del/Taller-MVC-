# Taller: Desarrollo Web con el Patrón MVC en Django

Repositorio con material y un scaffold básico para un taller práctico sobre el patrón MVC/MTV usando Django.

Recomendaciones:
- Python: 3.11 (o 3.10+)
- Django: 4.2 (LTS)

Cómo ejecutar (Linux/macOS):

```bash
# crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# instalar dependencias
pip install -r requirements.txt

# aplicar migraciones y crear superusuario opcional
python project_taller/manage.py migrate
python project_taller/manage.py createsuperuser

# ejecutar servidor
python project_taller/manage.py runserver
```

La aplicación principal está en `project_taller/tareas`. Contiene un modelo `Tarea`, vistas para listar, crear, editar, eliminar y marcar completada, y plantillas básicas en `project_taller/templates`.
# Taller-MVC-
# Guía del estudiante — Taller MVC con Django

Requisitos previos
- Python 3.10+ (recomendado 3.11)
- pip
- Conocimientos básicos de Python y HTML/CSS

Configuración rápida

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python project_taller/manage.py migrate
python project_taller/manage.py runserver
```

Estructura importante
- `project_taller/` — proyecto Django
- `project_taller/tareas/` — app con modelo `Tarea`, vistas y templates
- `project_taller/templates/` — plantillas globales
- `project_taller/static/` — CSS y archivos estáticos

Objetivo práctico
- Implementar y entender las partes MVC/MTV: modelo (datos), vistas (controladores) y templates (vistas renderizadas).

Tareas mínimas a completar durante el taller
1. Crear una tarea desde la interfaz.
2. Editar una tarea existente.
3. Marcar una tarea como completada / reabrir.
4. Eliminar una tarea (con confirmación).

Buenas prácticas
- Mantener las vistas sencillas y delegar validación a los formularios.
- Usar `reverse` o `url` en plantillas para construir rutas.
- Probar cambios ejecutando migraciones y revisando la interfaz.

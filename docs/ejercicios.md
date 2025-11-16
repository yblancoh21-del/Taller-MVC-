# Ejercicios guiados

Ejercicio 1 — Editar y validar
- Añade validaciones al `TareaForm`: título obligatorio y longitud mínima.
- Mostrar mensajes de error en la plantilla `form.html`.

Ejercicio 2 — Buscar tareas
- Añade un formulario de búsqueda en `lista.html`.
- Implementa lógica en `lista_tareas` para filtrar por `titulo`.

Ejercicio 3 — Paginación
- Usa `django.core.paginator.Paginator` para mostrar 5 tareas por página.
- Añade controles "Anterior / Siguiente" en la plantilla.

Ejercicio 4 — Autenticación (opcional)
- Protege la creación/edición/eliminación para usuarios autenticados.
- Añade vistas de login/logout o usa `django.contrib.auth.views`.

Ejercicio 5 — Tests básicos
- Escribe pruebas unitarias para:
  - Crear una tarea (POST a `nueva/`).
  - Marcar completada (toggle).
  - Listado de tareas muestra las tareas existentes.

Sugerencia: dividir los ejercicios entre pares y asignar 15-20 min por ejercicio.

# Plan del Taller: Desarrollo Web con el Patrón MVC en Django

Objetivo
- Que los estudiantes comprendan el patrón MVC/MTV y construyan una aplicación web simple en Django (lista de tareas).

Resultados de aprendizaje
- Entender la separación de responsabilidades (Model, View, Template).
- Crear modelos y usar el ORM de Django.
- Definir vistas y rutas (URLs) para la lógica de negocio.
- Crear plantillas y trabajar con archivos estáticos.
- Añadir operaciones CRUD básicas en una app real.

Agenda (4 horas sugeridas)

1. Introducción al MVC y Django — 30 min
- Conceptos del patrón MVC y diferencias con MTV.
- Ventajas de Django.

2. Configuración del entorno — 20 min
- Virtualenv, instalar dependencias (`requirements.txt`).
- Estructura del proyecto generado.

3. Modelo y ORM — 35 min
- Explicar `models.py`.
- Crear el modelo `Tarea` y aplicar migraciones.

4. Vistas y URLs — 35 min
- Crear vistas para listar, crear, editar, eliminar y alternar completado.
- Configurar `urls.py`.

5. Plantillas y static — 30 min
- Sistema de templates, `base.html` y bloques.
- Añadir CSS y servir archivos estáticos en desarrollo.

6. Práctica guiada — 60 min
- Los estudiantes implementan funcionalidades extra: editar, marcar completada, buscar, paginar.
- Integrar mensajes y validaciones.

7. Cierre y evaluación — 10 min
- Revisión de entregables, dudas y siguiente pasos.

Notas para el instructor
- Preparar un entorno de demostración con el scaffold en `project_taller/`.
- Mostrar primero la versión mínima (listar y crear) y luego extender.
- Incentivar preguntas y revisiones en parejas.

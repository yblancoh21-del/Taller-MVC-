# Soluciones (resumen)

Solución ejercicio 1 — Validación
- En `tareas/forms.py`:

```py
from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'completada']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if len(titulo) < 3:
            raise forms.ValidationError('El título debe tener al menos 3 caracteres.')
        return titulo
```

Solución ejercicio 2 — Búsqueda
- Añadir un input en `lista.html` que envíe `?q=...` y en la vista:

```py
q = request.GET.get('q')
if q:
    tareas = tareas.filter(titulo__icontains=q)
```

Solución ejercicio 3 — Paginación
- Usar `Paginator(tareas, 5)` y pasar la página a la plantilla.

Solución ejercicio 4 — Autenticación
- Decorar vistas con `@login_required` y usar `LoginView`/`LogoutView`.

Solución ejercicio 5 — Tests
- Usar `django.test.TestCase` y el cliente de pruebas `self.client` para POST/GET.

from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
    path('', views.lista_tareas, name='lista'),
    path('nueva/', views.crear_tarea, name='crear'),
    path('editar/<int:pk>/', views.editar_tarea, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_tarea, name='eliminar'),
    path('toggle/<int:pk>/', views.toggle_completada, name='toggle'),
]

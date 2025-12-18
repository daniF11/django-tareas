from django.urls import path
from . import views

urlpatterns = [
    #path('', views.inicio, name='saludo'),
    path('', views.lista_tareas, name='lista'),
    path('crear/', views.crear_tarea, name='crear'),
    path('toggle/<int:pk>/', views.toggle_tarea, name='toggle'),
    path('editar/<int:pk>/', views.editar_tarea, name='editar'),
    path('borrar/<int:pk>/', views.borrar_tarea, name='borrar'),



]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.mi_vista),
    path('login', views.iniciar_sesion, name='iniciar-sesion'),
    path('registro', views.registrarse , name='registrarse'),

    path('api/crear/', views.CourseCreate.as_view(), name='crear-curso'),
    path('api/eliminar/<int:Curso_id>/', views.CourseDelete.as_view(), name='eliminar-curso'),
    path('api/crear/inscripcion/', views.InscripcionCreate.as_view(), name='crear-iscripcion'),
]
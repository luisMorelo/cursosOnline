from django.urls import path
from .import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.mi_vista_principal, name='mi_vista_principal'),
    path('login', views.iniciar_sesion, name='iniciar-sesion'),
    path('registro', views.registrarse , name='registrarse'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar-sesion'),

    path('api/crear/', views.CourseCreate.as_view(), name='crear-curso'),
    path('api/eliminar/<int:Curso_id>/', views.CourseDelete.as_view(), name='eliminar-curso'),
    path('api/crear/inscripcion/', views.InscripcionCreate.as_view(), name='crear-iscripcion'),
]
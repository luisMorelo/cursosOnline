from django.urls import path
from .import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.mi_vista_principal, name='mi_vista_principal'),
    path('login', views.iniciar_sesion, name='iniciar-sesion'),
    path('registro', views.registrarse , name='registrarse'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar-sesion'),

    path('dashboard-usuario/', views.dashboard, name='dashboard-usuario'),
    path('dashboard-instructor/', views.dashboard_instructor, name='dashboard-instructor'),
    path('cursos-instructor/', views.cursos_instructor, name='cursos-instructor'),

    path('creando-curso/', views.crear_curso, name='crear-curso'),
    path('editar/<int:curso_id>/', editar_curso, name='editar-curso'),
    path('eliminar/<int:curso_id>/', eliminar_curso, name='eliminar-curso'),

    

    
    path('api/crear/', views.CourseCreate.as_view(), name='crear_curso'),
    path('api/eliminar/<int:Curso_id>/', views.CourseDelete.as_view(), name='eliminar_curso'),
    path('api/crear/inscripcion/', views.InscripcionCreate.as_view(), name='crear-iscripcion'),
]
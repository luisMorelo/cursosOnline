from django.urls import path

from aprendeOnline import settings
from .import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static



urlpatterns = [

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.mi_vista_principal, name='mi_vista_principal'),
    path('login', views.iniciar_sesion, name='iniciar-sesion'),
    path('registro', views.registrarse , name='registrarse'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar-sesion'),

    path('dashboard-usuario/', views.dashboard, name='dashboard-usuario'),
    path('dashboard-instructor/', views.dashboard_instructor, name='dashboard-instructor'),
    path('cursos-instructor/', views.cursos_instructor, name='cursos-instructor'),
    path('cursos-usuario/', views.cursos_usuario, name='cursos-usuario'),
    path('curso/<int:curso_id>/',views.contenido_curso_instructor, name='curso'),
    path('curso/<int:curso_id>/',views.contenido_curso_usuario, name='curso-usuario'),

    path('creando-curso/', views.crear_curso, name='crear-curso'),
    path('creando-examen/<int:curso_id>/',views.crear_examen, name='crear-examen'),
    path('subiendo-material/<int:curso_id>/',views.subir_material, name='subir-material'),
    path('editar/<int:curso_id>/',views.editar_curso, name='editar-curso'),
    path('eliminar/<int:curso_id>/',views.eliminar_curso, name='eliminar-curso'),

    path('inscribirse_curso/<int:curso_id>/', views.inscribirse_curso, name='inscribirse_curso'),
    path('cursos_usuario/', views.cursos_usuario, name='cursos_usuario'),
    path('curso-usuario/<int:curso_id>/', views.contenido_curso_usuario, name='contenido_curso_usuario'),
    path('examen/<int:examen_id>/', views.realizar_examen, name='realizar_examen'),


    

    

    
    path('api/crear/', views.CourseCreate.as_view(), name='crear_curso'),
    path('api/eliminar/<int:Curso_id>/', views.CourseDelete.as_view(), name='eliminar_curso'),
    path('api/crear/inscripcion/', views.InscripcionCreate.as_view(), name='crear-iscripcion'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
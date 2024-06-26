from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import Curso, Inscripcion, Examen, Material, Instructor, Respuesta, Opcion, Pregunta
from rest_framework import generics, permissions
from .serializers import cursoSerializer, InscripcionSerializer
from .forms import LoginForms, CursoForm, InscripcionForm, SingUpForm, MaterialForm, ExamenForm, RespuestaExamenForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class CourseList(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class CourseCreate(generics.CreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class CourseDetail(generics.RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class CourseUpdate(generics.UpdateAPIView):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class CourseDelete(generics.DestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    #permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación




#--------- Vistas vasadas en clase para el modelo Inscripciones ------

class InscripcionList(generics.ListAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class InscripcionCreate(generics.CreateAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class InscripcionDetail(generics.RetrieveAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class InscripcionUpdate(generics.UpdateAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class InscripcionDelete(generics.DestroyAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer 
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación



#Iniciar Sesión 
def iniciar_sesion(request):
    if request.method == 'GET':
        form = LoginForms()
        return render(request, 'login.html', {"form": form})
    else:
        form = LoginForms(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                if es_instructor(user):
                    return redirect('dashboard-instructor')
                else:
                    return redirect('dashboard-usuario')
            else:
                return render(request, 'login.html', {"form": form, "error": "El usuario o la contraseña son incorrectos"})
        else:
            return render(request, 'login.html', {"form": form, "error": "Por favor, corrija los errores del formulario"})
    

#Crear una cuenta
def registrarse(request):

    form = SingUpForm()
    if request.method == 'GET':
        return render(request,'register.html', {
            'form': form
        })
    else:
        if request.method == 'POST':

            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                user.save()
                login(request, user)
                
                return render(request, 'register.html', {'form': form, 'exito': '¡El usuario fue creado exitósamente!'})
            else:
                return render(request, 'register.html', {'form': form, 'error': 'Las contraseñas no coinciden, verifica e intentalo de nuevo'})
         

@login_required
def dashboard(request):
    nombre_usuario = request.user.username  # Obtiene el nombre de usuario del usuario autenticado
    cursos = Curso.objects.all()
    return render(request, 'usuario-dashboard.html', { 
        'nombres_usuarios': nombre_usuario, 
        'cursos': cursos
    })



#Vista pincipal sin loguearse
def mi_vista_principal(request):
    if request.method == 'GET':
        return render(request, 'index.html')




#cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('mi_vista_principal')  # Redirigir a la página de inicio de sesión después de cerrar sesión




@login_required
def dashboard_instructor(request):
    nombre_usuario = request.user.username  # Obtiene el nombre de usuario del usuario autenticado
    cursos = Curso.objects.all()
    return render(request, 'instructor-dashboard.html', { 
        'nombres_usuarios': nombre_usuario,
        'cursos': cursos
    })




#Vista de cursos creados por el intructor
@login_required
def cursos_instructor(request):

    cursos = Curso.objects.all()
    nombre_usuario = request.user.username
    form = CursoForm()

    if request.method == 'GET':
        return render(request, 'cursos-instructor.html', {
            'form': form, 
            'nombres_usuarios': nombre_usuario,
            'cursos': cursos 
        })
    

    

# como objetivo verificar si un usuario tiene el rol de instructor. 
# Esto se logra comprobando si el usuario tiene un objeto relacionado de tipo Instructor. 
# En Django, esto se hace utilizando la función hasattr.
def es_instructor(user):
    return hasattr(user, 'instructor')


@user_passes_test(es_instructor)
@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.instructor = request.user.instructor
            curso.save()
            return redirect('cursos-instructor')
        else:
            return render(request, 'crear-curso.html', {'form': form, 'error': 'Formulario no válido. Por favor, corrige los errores.'})
    else:
        form = CursoForm()
    
    return render(request, 'crear-curso.html', {'form': form})



@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})



@user_passes_test(es_instructor)
@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, instructor=request.user.instructor)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos-instructor')
        else:
            return render(request, 'editar-curso.html', {'form': form, 'curso': curso, 'error': 'Formulario no válido. Por favor, corrige los errores.'})
    else:
        form = CursoForm(instance=curso)
    
    return render(request, 'editar-curso.html', {'form': form, 'curso': curso})





@user_passes_test(es_instructor)
@login_required
def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, instructor=request.user.instructor)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos-instructor')
    
    return render(request, 'eliminar-curso.html', {'curso': curso})


@login_required
def contenido_curso_instructor(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id, instructor=request.user.instructor)
    nombre_usuario = request.user.username
    cursos = Curso.objects.all()
    examenes = Examen.objects.filter(curso=curso)  # Filtra los exámenes por el curso
    materiales = Material.objects.filter(curso=curso)  # Filtra los materiales por el curso

    if request.method == 'GET':
        return render(request, 'vista-curso-intructor.html', {
            'curso': curso, 
            'nombres_usuarios': nombre_usuario,
            'cursos': cursos, 
            'examenes': examenes,  # Pasa los exámenes filtrados al contexto
            'materiales': materiales  # Pasa los materiales filtrados al contexto
        })




@login_required
def crear_examen(request, curso_id):
    nombre_usuario = request.user.username
    curso = get_object_or_404(Curso, id=curso_id, instructor=request.user.instructor)
    cursos = Curso.objects.all()

    if request.method == 'GET':
        form = ExamenForm()
        return render(request, 'diseñar-examen.html', {
            'curso': curso,
            'nombres_usuarios': nombre_usuario,
            'cursos': cursos,
            'form': form
        })
    else:
        form = ExamenForm(request.POST)
        if form.is_valid():
            examen = form.save(commit=False)
            examen.curso = curso  # Asignar el curso correcto
            examen.save()
            return redirect('curso', curso_id=curso_id)  # Redirigir al curso correcto
        else:
            return render(request, 'diseñar-examen.html', {
                'curso': curso,
                'nombres_usuarios': nombre_usuario,
                'cursos': cursos,
                'form': form,
                'error': 'No se pudo guardar el examen'
            })




@login_required
def subir_material(request, curso_id):
    nombre_usuario = request.user.username
    curso = get_object_or_404(Curso, id=curso_id, instructor=request.user.instructor)
    cursos = Curso.objects.all()

    if request.method == 'GET':
        form = MaterialForm()
        return render(request, 'subir-material.html', {
            'curso': curso,
            'nombres_usuarios': nombre_usuario,
            'cursos': cursos, 
            'form': form
        })
    else:

        form = MaterialForm(request.POST, request.FILES)  # manejo de request.FILES para subir archivo
        if form.is_valid():
            material = form.save(commit=False)
            material.curso = curso  # Asignar el curso correcto
            material.save()
            return redirect('curso', curso_id=curso_id)  # Redirigir al curso correcto
        else:
            return render(request, 'subir-material.html', {
                'curso': curso,
                'nombres_usuarios': nombre_usuario,
                'cursos': cursos, 
                'form': form,
                'error': 'No se pudo guardar el material'  
            })



'''
Vistas para el rol de usuario
'''


#Inscripción en un curso
@login_required
def inscribirse_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    Inscripcion.objects.get_or_create(user=request.user, curso=curso)
    return redirect('cursos_usuario')


#Vista de cursos a los que se ha inscrito un usuario
@login_required
def cursos_usuario(request):
    inscripciones = Inscripcion.objects.filter(user=request.user)
    cursos = [inscripcion.curso for inscripcion in inscripciones]
    nombre_usuario = request.user.username

    return render(request, 'cursos-usuario.html', {
        'nombre_usuario': nombre_usuario,
        'cursos': cursos
    })




#Ver contenido del curso
@login_required
def contenido_curso_usuario(request, curso_id):
    # Verificar si el usuario está inscrito en el curso
    inscripcion = get_object_or_404(Inscripcion, curso_id=curso_id, user=request.user)
    curso = inscripcion.curso  # Obtener el curso a partir de la inscripción
    nombre_usuario = request.user.username
    examenes = Examen.objects.filter(curso=curso)  # Filtrar los exámenes por el curso
    materiales = Material.objects.filter(curso=curso)  # Filtrar los materiales por el curso

    return render(request, 'vista-curso-usuario.html', {
        'curso': curso, 
        'nombre_usuario': nombre_usuario,
        'examenes': examenes,  # Pasar los exámenes filtrados al contexto
        'materiales': materiales  # Pasar los materiales filtrados al contexto
    })



#Realizar un examen
@login_required
def realizar_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    nombre_usuario = request.user.username

    if request.method == 'POST':
        form = RespuestaExamenForm(request.POST)
        if form.is_valid():
            for pregunta in examen.preguntas.all():
                opcion_id = request.POST.get(f'pregunta_{pregunta.id}')
                if opcion_id:
                    opcion = Opcion.objects.get(id=opcion_id)
                    Respuesta.objects.create(
                        user=request.user,
                        pregunta=pregunta,
                        opcion=opcion
                    )
            return redirect('contenido_curso_usuario', curso_id=examen.curso.id)
    else:
        form = RespuestaExamenForm()

    return render(request, 'realizar-examen.html', {
        'nombre_usuario': nombre_usuario,
        'examen': examen,
        'form': form
    })





@login_required
def tomar_examen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    preguntas = Pregunta.objects.filter(examen=examen).prefetch_related('opciones')
    
    if request.method == 'POST':
        for pregunta in preguntas:
            opcion_id = request.POST.get(f'pregunta_{pregunta.id}')
            if opcion_id:
                opcion = get_object_or_404(Opcion, id=opcion_id)
                Respuesta.objects.create(user=request.user, pregunta=pregunta, opcion=opcion)
        return redirect('examen_resultado', examen_id=examen.id)
    
    return render(request, 'tomar-examen.html', {
        'examen': examen,
        'preguntas': preguntas
    })

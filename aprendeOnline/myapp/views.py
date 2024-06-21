from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import Curso, Inscripcion
from rest_framework import generics, permissions
from .serializers import cursoSerializer, InscripcionSerializer
from .forms import LoginForms, CursoForm, InscripcionForm, SingUpForm
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
    


@login_required
def dashboard(request):
    nombre_usuario = request.user.username  # Obtiene el nombre de usuario del usuario autenticado
    return render(request, 'usuario-dashboard.html', { 'nombres_usuarios': nombre_usuario })



@login_required
def dashboard_instructor(request):
    nombre_usuario = request.user.username  # Obtiene el nombre de usuario del usuario autenticado
    return render(request, 'instructor-dashboard.html', { 'nombres_usuarios': nombre_usuario })


#cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('mi_vista_principal')  # Redirigir a la página de inicio de sesión después de cerrar sesión



#Vista pincipal sin loguearse
def mi_vista_principal(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    

    
#Vista de cursos creados por el intructor
@login_required
def cursos_instructor(request):

    nombre_usuario = request.user.username
    form = CursoForm()

    if request.method == 'GET':
        return render(request, 'cursos-instructor.html', {
            'form': form, 
            'nombres_usuarios': nombre_usuario 
        })


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
            

# como objetivo verificar si un usuario tiene el rol de instructor. 
# Esto se logra comprobando si el usuario tiene un objeto relacionado de tipo Instructor. 
# En Django, esto se hace utilizando la función hasattr.
def es_instructor(user):
    return hasattr(user, 'instructor')




@user_passes_test(es_instructor)
@login_required
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.instructor = request.user.instructor
            curso.save()
            return redirect('cursos-instructor')
    else:
        form = CursoForm()
    return render(request, 'crear-curso.html', {'form': form})




@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})
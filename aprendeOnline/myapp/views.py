from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {"form": form, "error": "El usuario o la contraseña son incorrectos"})
        else:
            return render(request, 'login.html', {"form": form, "error": "Por favor, corrija los errores del formulario"})
    


@login_required
def dashboard(request):
    nombre_usuario = request.user.username  # Obtiene el nombre de usuario del usuario autenticado
    return render(request, 'dashboard.html', { 'nombres_usuarios': nombre_usuario })


#cerrar sesion
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('mi_vista_principal')  # Redirigir a la página de inicio de sesión después de cerrar sesión



#Vista pincipal sin loguearse
def mi_vista_principal(request):
    if request.method == 'GET':
        return render(request, 'index.html')


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
            



def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})
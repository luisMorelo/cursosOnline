from django.shortcuts import render

# Create your views here.
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




def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html')



def mi_vista(request):
    if request.method == 'GET':
        return render(request, 'index.html')


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
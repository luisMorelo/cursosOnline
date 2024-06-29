# cursosOnline
# Plataforma de Cursos en Línea

## Descripción

Esta es una plataforma de cursos en línea desarrollada con Django que permite a los usuarios inscribirse en cursos, ver material educativo y realizar exámenes. Los instructores pueden crear, editar y eliminar cursos, así como subir material y diseñar exámenes.

## Características

- Registro e inicio de sesión de usuarios
- Inscripción en cursos
- Visualización de material educativo
- Realización de exámenes
- Gestión de cursos y material educativo por parte de los instructores

## Requisitos

- Python 3.8+
- Django 3.2+
- Virtualenv

## Instalación

1. Clona el repositorio

    ```bash
    git clone https://github.com/tu-usuario/tu-repositorio.git
    cd tu-repositorio
    ```

2. Crea y activa un entorno virtual

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos

    ```bash
    python manage.py migrate
    ```

5. Carga los datos iniciales (opcional)

    ```bash
    python manage.py loaddata initial_data.json
    ```

6. Ejecuta el servidor de desarrollo

    ```bash
    python manage.py runserver
    ```

7. Crea un super usuario para gestionar los modelos 
   ```bash
    python manage.py createsuperuser (pulsa enter y crea tus credenciales)
    ``` 









## Configuración

### Variables de Entorno

Asegúrate de configurar las siguientes variables de entorno en tu archivo `.env` o en tu entorno de ejecución:

- `SECRET_KEY`: La clave secreta de Django.
- `DEBUG`: Establecer a `True` para el desarrollo y `False` para producción.
- `DATABASE_URL`: La URL de conexión a la base de datos.

Ejemplo de archivo `.env`:

```plaintext
SECRET_KEY=tu_clave_secreta
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

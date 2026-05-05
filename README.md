# GameHub - Aplicación de Videojuegos

Aplicación web para gestionar videojuegos y reseñas. Permite a los usuarios registrarse, crear perfiles, compartir juegos y escribir reseñas con puntuaciones.

## Características principales

- Sistema completo de autenticación (registro, login, logout)
- CRUD de videojuegos con imágenes
- Sistema de reseñas con calificación (1-5 estrellas)
- Perfil de usuario con historial de actividad
- Búsqueda de juegos por título, descripción y categoría
- Paginación en listados
- Control de permisos (solo el autor puede editar/eliminar sus contenidos)
- Interfaz responsive con Bootstrap 5
- Tema claro/oscuro con persistencia en cookies
- Rating promedio calculado automáticamente

## Tecnología utilizada

- Django 6.0.4
- PostgreSQL (Docker) / SQLite (desarrollo local)
- Bootstrap 5
- Python 3.12
- Docker y Docker Compose

## Instalación y ejecución

### Requisitos previos
- Docker
- Docker Compose

### Pasos de instalación

1. Navegar al directorio del proyecto:
```bash
cd /home/lucas/Escritorio/GameHub
```

2. Ejecutar con Docker:
```bash
docker-compose up --build
```

Este comando construirá la imagen, iniciará PostgreSQL y ejecutará las migraciones automáticamente. La aplicación estará disponible en http://localhost:8000

3. Crear superusuario (en otra terminal):
```bash
docker compose exec web python manage.py createsuperuser
```

4. Acceder a la aplicación:
- Interfaz principal: http://localhost:8000
- Panel de administración: http://localhost:8000/admin

5. Detener los contenedores:
```bash
docker-compose down
```

## Estructura del proyecto

```
GameHub/
├── config/                 # Configuración principal de Django
├── users/                  # App de gestión de usuarios
├── games/                  # App de gestión de videojuegos
├── reviews/                # App de reseñas
├── templates/              # Templates HTML
├── static/                 # Archivos estáticos (CSS, JS, imágenes)
├── media/                  # Imágenes subidas por usuarios
├── manage.py               # Interfaz de línea de comandos de Django
├── requirements.txt        # Dependencias Python
├── Dockerfile              # Configuración de Docker
├── docker-compose.yml      # Orquestación de servicios
├── .env                    # Variables de entorno
└── db.sqlite3              # Base de datos SQLite (desarrollo local)
```

## Apps del proyecto

### App Users
Gestiona el sistema de autenticación y perfil de usuario.
- Registro con validación de email único
- Login con opción "recuérdame" (mantiene sesión 30 días)
- Perfil de usuario con historial de juegos y reseñas
- Listados separados de "mis juegos" y "mis reseñas"

### App Games
Gestión completa de videojuegos (CRUD).
- Crear, editar, eliminar juegos
- Campos: título, descripción, imagen, categoría, fecha de lanzamiento
- Solo el autor puede editar/eliminar sus juegos
- Listado paginado con búsqueda

### App Reviews
Sistema de reseñas y calificaciones.
- Crear reseña con calificación (1-5 estrellas) y comentario
- Un usuario solo puede tener una reseña por juego
- Editar/eliminar propia reseña
- Rating promedio calculado automáticamente

## URLs principales

### Juegos
- `/juegos/` - Listado de todos los juegos
- `/juegos/game/<id>/` - Detalle de un juego
- `/juegos/crear/` - Crear nuevo juego (requiere login)
- `/juegos/game/<id>/editar/` - Editar juego (solo autor)
- `/juegos/game/<id>/eliminar/` - Eliminar juego (solo autor)

### Reseñas
- `/resenas/juego/<game_id>/crear/` - Crear reseña
- `/resenas/resena/<review_id>/editar/` - Editar reseña
- `/resenas/resena/<review_id>/eliminar/` - Eliminar reseña

### Usuarios
- `/usuarios/registro/` - Registro de nuevo usuario
- `/usuarios/login/` - Inicio de sesión
- `/usuarios/logout/` - Cerrar sesión
- `/usuarios/perfil/` - Perfil del usuario actual
- `/usuarios/mis-juegos/` - Juegos creados por el usuario
- `/usuarios/mis-resenas/` - Reseñas escritas por el usuario

## Configuración

### Base de datos
- En desarrollo local: SQLite (db.sqlite3)
- En producción con Docker: PostgreSQL

### Autenticación
- Las sesiones se almacenan en la base de datos
- Sin "recuérdame": sesión expira al cerrar el navegador
- Con "recuérdame": sesión persiste 30 días

### Tema claro/oscuro
- El tema preferido se guarda en una cookie de 365 días
- Se carga automáticamente al abrir la aplicación
- Se puede cambiar desde el perfil de usuario

## Comandos útiles (desarrollo local)

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# Entrar a shell de Django
python manage.py shell
```

## Panel de administración

El panel de administración en `/admin` permite:
- Gestionar usuarios, juegos y reseñas
- Filtrar y buscar registros
- Ver estadísticas de usuarios y juegos
- Acciones en lote

## Seguridad

- CSRF Token en todos los formularios
- Contraseñas hasheadas automáticamente
- Validación de permisos en backend
- Solo usuarios autenticados pueden crear contenido
- Solo el autor puede editar/eliminar sus contenidos
- Email único por usuario
- Contraseña fuerte requerida (mínimo 8 caracteres)

## Notas de desarrollo

- El proyecto usa SQLite en desarrollo local para simplificar la configuración
- Docker Compose incluye PostgreSQL configurado para producción
- Las imágenes se almacenan en la carpeta `media/games/`
- Los estilos CSS se encuentran en `static/css/estilos.css`
- Bootstrap 5 se carga desde CDN

## Requisitos de usuario

- El registro requiere un nombre de usuario único
- El email debe ser único
- La contraseña debe cumplir requisitos de seguridad
- Acceso a todas las características requiere estar autenticado

# GameHub - Aplicación de Videojuegos

Aplicación web para gestionar videojuegos y reseñas. Permite a los usuarios registrarse, crear perfiles, compartir juegos y escribir reseñas con puntuaciones.

## Características principales

- Landing page de bienvenida con presentación completa de características
- Sistema completo de autenticación (registro, login, logout)
- CRUD de videojuegos con imágenes, trailers de YouTube y clasificación PEGI
- Sistema de reseñas con calificación usando estrellas interactivas (1-5)
- Perfil de usuario con foto de perfil, historial de actividad
- Búsqueda de juegos por título, descripción y categoría
- Paginación en listados
- Control de permisos (solo el autor puede editar/eliminar sus contenidos)
- Interfaz responsive con Bootstrap 5
- Tema claro/oscuro con persistencia en cookies
- Rating promedio calculado automáticamente
- Logo y favicon personalizados
- Estrellas interactivas con hover effect para rating (amarillo con gris)
- Validación de formularios en frontend y backend
- Trailers integrados de YouTube
- Clasificaciones PEGI por edad

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

### Qué es requirements.txt

El archivo `requirements.txt` contiene todas las dependencias (librerías Python) necesarias para que el proyecto funcione. Especifica el nombre y versión exacta de cada paquete. Esto garantiza que tanto en desarrollo como en producción se usen las mismas versiones.

### Instalación con Docker (recomendado)

1. Navegar al directorio del proyecto:
```bash
cd /home/lucas/Escritorio/GameHub
```

2. Ejecutar con Docker:
```bash
docker-compose up --build
```

Este comando automáticamente:
- Construye la imagen Docker
- Instala las dependencias del `requirements.txt`
- Inicia PostgreSQL
- Ejecuta las migraciones
- Inicia el servidor en http://localhost:8000

3. En otra terminal, crear superusuario:
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

### Instalación local (desarrollo sin Docker)

Si prefieres trabajar sin Docker necesitas tener instalado Python 3.12:

1. Crear entorno virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependencias desde requirements.txt:
```bash
pip install -r requirements.txt
```

3. Aplicar migraciones:
```bash
python manage.py migrate
```

4. Crear superusuario:
```bash
python manage.py createsuperuser
```

5. Ejecutar servidor:
```bash
python manage.py runserver
```

## Estructura del proyecto

```
GameHub/
├── config/                 # Configuración principal de Django
├── home/                   # App de landing page
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

### App Home
Página de bienvenida y landing page.
- Landing page principal con presentación visual atractiva
- Sección hero con llamada a la acción
- Descripción de 9 características principales (Catálogo, Reseñas, Perfil, Añadir juegos, Comunidad, Trailers, PEGI, Búsqueda, Modo oscuro)
- Botones de navegación (Explorar Juegos, Registrarse)
- Diseño responsive adaptado a móvil
- Iconos Bootstrap para cada característica
- Interfaz consistente con el resto de la aplicación

### App Users
Gestiona el sistema de autenticación y perfil de usuario.
- Registro con validación de email único
- Login con opción "recuérdame" (mantiene sesión 30 días)
- Perfil de usuario con historial de juegos y reseñas
- Listados separados de "mis juegos" y "mis reseñas"

### App Games
Gestión completa de videojuegos (CRUD).
- Crear, editar, eliminar juegos
- Campos: título, descripción, imagen, categoría, fecha de lanzamiento y un trailer de YouTube
- Solo el autor puede editar/eliminar sus juegos
- Listado paginado con búsqueda

### App Reviews
Sistema de reseñas y calificaciones.
- Crear reseña con calificación (1-5 estrellas) mediante interfaz visual de estrellas
- Las estrellas tienen hover effect: se rellenan de amarillo al pasar el ratón
- Un usuario solo puede tener una reseña por juego
- Editar/eliminar propia reseña
- Rating promedio calculado automáticamente
- Comentarios opcionales para cada reseña

## URLs principales

### Home
- `/` - Landing page de bienvenida

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

### Variables de Entorno (.env)

El archivo `.env` contiene variables sensibles del proyecto:
- `DEBUG`: Modo debug (True en desarrollo, False en producción)
- `SECRET_KEY`: Clave secreta de Django para seguridad
- `DATABASE_URL`: Conexión a PostgreSQL en Docker
- `ALLOWED_HOSTS`: Hosts permitidos para acceder a la aplicación

No debe compartirse en control de versiones (está en .gitignore).

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

## Comandos útiles

### Sin Docker (desarrollo local)

```bash
# Instalar dependencias de requirements.txt
pip install -r requirements.txt

# Crear migraciones después de cambiar modelos
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Crear superusuario para acceder a /admin
python manage.py createsuperuser

# Ejecutar servidor de desarrollo
python manage.py runserver

# Entrar a consola interactiva de Django
python manage.py shell
```

### Con Docker

```bash
# Construir y ejecutar
docker-compose up --build

# Solo iniciar (sin rebuild)
docker-compose up

# Ejecutar comando en el contenedor web
docker compose exec web python manage.py makemigrations

# Ver logs en tiempo real
docker-compose logs -f web

# Detener
docker-compose down
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
- Los estilos CSS personalizados se encuentran en `static/css/estilos.css`
- Bootstrap 5 se carga desde CDN
- El logo de la aplicación (favicon) se encuentra en `static/imgs/imagen_logo.jpeg`
- Las estrellas interactivas de reseña usan CSS personalizado sin librerías externas

## Requisitos de usuario

- El registro requiere un nombre de usuario único
- El email debe ser único
- La contraseña debe cumplir requisitos de seguridad
- Acceso a todas las características requiere estar autenticado

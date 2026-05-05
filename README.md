# GameHub - Aplicación de Videojuegos

Aplicación web completa para gestionar videojuegos y reseñas, construida con Django siguiendo un nivel realista de estudiante DAW.

## Resumen del Proyecto ✅

**Funcionalidades principales:**
- ✅ Sistema de usuarios (registro, login, logout, remember me)
- ✅ CRUD completo de videojuegos
- ✅ Sistema de reseñas con rating (1-5 estrellas)
- ✅ Perfil de usuario con historial
- ✅ Permisos: solo autor puede editar/eliminar
- ✅ Búsqueda de juegos por título/descripción/categoría
- ✅ Rating promedio calculado automáticamente
- ✅ Paginación en listados
- ✅ Interfaz con Bootstrap 5 responsive

**Tecnología:**
- Django 6.0.4
- PostgreSQL (Docker) / SQLite (desarrollo local)
- Bootstrap 5
- Python 3.12
- Docker & Docker Compose

**Estructura completa:** 11 fases implementadas

## Requisitos previos
- Docker
- Docker Compose

## Instalación y ejecución

### 1. Clonar el proyecto
```bash
cd /home/lucas/Escritorio/GameHub
```

### 2. Ejecutar con Docker
```bash
docker-compose up --build
```

Este comando:
- Construye la imagen de Django
- Inicia PostgreSQL en el puerto 5432
- Ejecuta migraciones automáticamente
- Inicia el servidor en http://localhost:8000

### 3. Crear superusuario (en otra terminal)
```bash
docker compose exec web python manage.py createsuperuser
```

### 4. Acceder a la aplicación
- Aplicación: http://localhost:8000
- Admin: http://localhost:8000/admin

### 5. Detener los contenedores
```bash
docker-compose down
```

## Estructura del proyecto

```
GameHub/
├── config/              # Configuración de Django
├── users/               # App de usuarios (FASE 2)
├── games/               # App de juegos (FASE 2)
├── reviews/             # App de reseñas
├── templates/           # Templates HTML
├── static/              # Archivos estáticos (CSS, JS, img)
├── media/               # Archivos de usuarios (imágenes de juegos)
├── manage.py            # CLI de Django
├── requirements.txt     # Dependencias Python
├── Dockerfile           # Configuración Docker
├── docker-compose.yml   # Orquestación de servicios
├── .env                 # Variables de entorno
└── db.sqlite3          # Base de datos SQLite (desarrollo local)
```

## FASE 1 ✅ - Estructura básica + Docker + PostgreSQL
- ✅ `requirements.txt`: Django 6.0.4, psycopg2, python-decouple, Pillow
- ✅ `.env`: Variables de entorno configurables
- ✅ `Dockerfile`: Imagen Docker con Python 3.12
- ✅ `docker-compose.yml`: PostgreSQL + Django con healthcheck
- ✅ `config/settings.py`: Configuración con variables de entorno

## FASE 2 ✅ - Apps y configuración básica
- ✅ App **users**: Sistema de usuarios (registro, login, logout)
- ✅ App **games**: Gestión de videojuegos (CRUD)
- ✅ App **reviews**: Sistema de reseñas (CRUD)
- ✅ `settings.py` actualizado:
  - Apps instaladas: users, games, reviews
  - Configuración de static/media
  - URLs de login/logout configuradas
- ✅ Migraciones iniciales aplicadas
- ✅ `.env` configurado para SQLite en desarrollo local

## FASE 3 ✅ - Modelos Game y Review
- ✅ **Modelo Game** (`games/models.py`):
  - title: CharField (200 caracteres)
  - description: TextField
  - image: ImageField (carpeta 'games/')
  - category: CharField con opciones (Acción, Aventura, RPG, Estrategia, Deporte, Simulación)
  - release_date: DateField (nullable)
  - created_by: ForeignKey → User
  - created_at, updated_at: timestamps automáticos
  - Ordenamiento: por fecha de creación descendente

- ✅ **Modelo Review** (`reviews/models.py`):
  - game: ForeignKey → Game (elimina reseñas al borrar juego)
  - user: ForeignKey → User (elimina reseñas al borrar usuario)
  - rating: IntegerField con opciones (1-5 estrellas)
  - comment: TextField
  - created_at, updated_at: timestamps automáticos
  - unique_together: (game, user) - Una reseña por usuario por juego
  - Ordenamiento: por fecha de creación descendente

- ✅ **Admin registrado**:
  - GameAdmin: Listado con título, categoría, fecha, autor; filtros y búsqueda
  - ReviewAdmin: Listado con usuario, juego, rating; filtros por rating y juego

- ✅ **Migraciones aplicadas**:
  - `games/migrations/0001_initial.py`: Crear tabla Game
  - `reviews/migrations/0001_initial.py`: Crear tabla Review (depende de Game)

## FASE 4 ✅ - Formularios
- ✅ **GameForm** (`games/forms.py`):
  - Campos: title, description, image, category, release_date
  - Widgets Bootstrap para HTML form
  - Campos de texto con placeholder
  - Selector de fecha HTML5 (type="date")
  - Sin campo created_by (se asigna en la vista)

- ✅ **ReviewForm** (`reviews/forms.py`):
  - Campos: rating, comment
  - Rating con RadioSelect widget para seleccionar estrellas (1-5)
  - Textarea para comentario con placeholder
  - Diseño simple sin modelo de usuario (se asigna en la vista)
  - Sin campo game/user (se asignan en la vista)

- ✅ **Validación automática**:
  - Django valida required fields
  - rating solo acepta valores 1-5
  - Comment es requerido
  - Title y description requieren contenido

## FASE 5 ✅ - Vistas CRUD de Games
- ✅ **GameListView** - Listado de todos los juegos
  - Vista genérica ListView
  - Paginación: 12 juegos por página
  - URL: `/juegos/`
  - Template: `games/game_list.html`

- ✅ **GameDetailView** - Detalle de un juego
  - Vista genérica DetailView
  - URL: `/juegos/game/<id>/`
  - Template: `games/game_detail.html`

- ✅ **GameCreateView** - Crear nuevo juego
  - Requiere login (LoginRequiredMixin)
  - Asigna automáticamente `created_by = request.user`
  - URL: `/juegos/crear/`
  - Template: `games/game_form.html`
  - Redirección: GameListView

- ✅ **GameUpdateView** - Editar juego
  - Requiere login + solo el autor puede editar (UserPassesTestMixin)
  - Si no es el autor, redirige a detail
  - URL: `/juegos/game/<id>/editar/`
  - Template: `games/game_form.html`
  - Redirección: GameListView

- ✅ **GameDeleteView** - Eliminar juego
  - Requiere login + solo el autor puede eliminar
  - Si no es el autor, redirige a detail
  - URL: `/juegos/game/<id>/eliminar/`
  - Template: `games/game_confirm_delete.html`
  - Redirección: GameListView

- ✅ **URLs configuradas** (`games/urls.py`):
  - Namespace: `games`
  - Rutas simples y claras
  - Nombres reutilizables en templates

- ✅ **config/urls.py actualizado**:
  - Include de games.urls bajo `/juegos/`
  - Soporte para MEDIA_URL y STATIC_URL en DEBUG
  - Listo para servir archivos de usuarios

## FASE 6 ✅ - Reseñas CRUD (Create, Edit, Delete)
- ✅ **ReviewCreateView** - Crear reseña desde juego
  - Requiere login (LoginRequiredMixin)
  - Asigna automáticamente game y user
  - Valida unique_together (una reseña por usuario por juego)
  - Si ya existe reseña → muestra error en formulario
  - URL: `/resenas/juego/<game_id>/crear/`
  - Template: `reviews/review_form.html`
  - Redirección: GameDetailView del juego

- ✅ **ReviewUpdateView** - Editar reseña
  - Requiere login + ser el autor (UserPassesTestMixin)
  - Si no es el autor → redirige a detail del juego
  - URL: `/resenas/resena/<review_id>/editar/`
  - Template: `reviews/review_form.html`
  - Redirección: GameDetailView del juego

- ✅ **ReviewDeleteView** - Eliminar reseña
  - Requiere login + ser el autor
  - Si no es el autor → redirige a detail del juego
  - URL: `/resenas/resena/<review_id>/eliminar/`
  - Template: `reviews/review_confirm_delete.html`
  - Redirección: GameDetailView del juego

- ✅ **URLs configuradas** (`reviews/urls.py`):
  - Namespace: `reviews`
  - URLs simples y claras
  - Parámetro game_pk para crear (FK del juego)
  - Parámetro pk para editar/eliminar (PK de la reseña)

- ✅ **config/urls.py actualizado**:
  - Include de reviews.urls bajo `/resenas/`
  - Integrado con games.urls

## FASE 7 ✅ - Sistema de Usuarios (Registro, Login, Logout, Remember Me)

- ✅ **RegisterView** - Registro de nuevos usuarios
  - Formulario: `RegisterForm` (extends UserCreationForm)
  - Campos: username, email, first_name, last_name, password1, password2
  - Validación: email único + contraseña fuerte
  - URL: `/usuarios/registro/` → `users:register`
  - Template: `users/register.html`
  - Redirección: Login

- ✅ **CustomLoginView** - Inicio de sesión
  - Formulario: `LoginForm` (extends AuthenticationForm)
  - Campos: username, password, remember_me (checkbox)
  - Remember me: Sesión persistente por 30 días
  - URL: `/usuarios/login/` → `users:login`
  - Template: `users/login.html`
  - Redirección: GameListView

- ✅ **CustomLogoutView** - Cerrar sesión
  - URL: `/usuarios/logout/` → `users:logout`
  - Redirección: GameListView

- ✅ **Formularios** (`users/forms.py`):
  - **RegisterForm**: UserCreationForm personalizado
    - Valida email único
    - Campos con estilos Bootstrap
    - Validación de contraseña integrada
  - **LoginForm**: AuthenticationForm personalizado
    - Campo "remember_me" como checkbox
    - Campos con estilos Bootstrap

- ✅ **Configuración de sesiones** (`config/settings.py`):
  - `LOGIN_URL = 'users:login'`
  - `LOGIN_REDIRECT_URL = 'games:game_list'`
  - `LOGOUT_REDIRECT_URL = 'games:game_list'`
  - `SESSION_ENGINE = 'django.contrib.sessions.backends.db'`
  - `SESSION_COOKIE_AGE = 1209600` (2 semanas por defecto)
  - `SESSION_EXPIRE_AT_BROWSER_CLOSE = True` (sin remember me)

- ✅ **Lógica Remember Me**:
  - Sin remember me: sesión expira al cerrar navegador
  - Con remember me: sesión persiste 30 días
  - Implementado con `session.set_expiry()`

- ✅ **URLs configuradas** (`users/urls.py`):
  - `/usuarios/registro/` → Registro
  - `/usuarios/login/` → Login
  - `/usuarios/logout/` → Logout

## FASE 8 ✅ - Permisos Básicos

**Matriz de Permisos:**

| Acción | No logueado | Logueado | Autor | No autor |
|--------|------------|----------|-------|----------|
| **Ver listado juegos** | ✅ | ✅ | ✅ | ✅ |
| **Ver detalle juego** | ✅ | ✅ | ✅ | ✅ |
| **Crear juego** | ❌ Redirige a login | ✅ | - | - |
| **Editar juego** | ❌ Redirige a login | ❌ Redirige a detail | ✅ | ❌ Redirige a detail |
| **Eliminar juego** | ❌ Redirige a login | ❌ Redirige a detail | ✅ | ❌ Redirige a detail |
| **Ver reseñas** | ✅ | ✅ | ✅ | ✅ |
| **Crear reseña** | ❌ Redirige a login | ✅ (una por juego) | - | - |
| **Editar reseña** | ❌ Redirige a login | ❌ Redirige a detail | ✅ | ❌ Redirige a detail |
| **Eliminar reseña** | ❌ Redirige a login | ❌ Redirige a detail | ✅ | ❌ Redirige a detail |

**Implementación por Mixin:**

- **LoginRequiredMixin**:
  - Usado en: GameCreateView, ReviewCreateView
  - Comportamiento: Si no está logueado → redirige a `LOGIN_URL`
  - Configurado en settings: `LOGIN_URL = 'users:login'`

- **UserPassesTestMixin**:
  - Usado en: GameUpdateView, GameDeleteView, ReviewUpdateView, ReviewDeleteView
  - Método: `test_func()` verifica:
    - Game: `self.request.user == game.created_by`
    - Review: `self.request.user == review.user`
  - Si falla: `handle_no_permission()` redirige al detail del recurso

**Validaciones Especiales:**

- **unique_together (game, user) en Review**:
  - Un usuario solo puede tener 1 reseña por juego
  - Si intenta crear otra → IntegrityError → mensaje en formulario
  - Solución: Editar la reseña existente

**Permisos en Templates (condicionales):**

```django
{# Solo mostrar botón crear si está logueado #}
{% if user.is_authenticated %}
  <a href="{% url 'games:game_create' %}">Crear juego</a>
{% else %}
  <p>Inicia sesión para crear juegos</p>
{% endif %}

{# Solo mostrar botones editar/eliminar si es el autor #}
{% if game.created_by == user %}
  <a href="{% url 'games:game_update' game.pk %}">Editar</a>
  <a href="{% url 'games:game_delete' game.pk %}">Eliminar</a>
{% endif %}

{# Protección en formularios #}
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Guardar</button>
</form>
```

**Seguridad Implementada:**

- ✅ CSRF Token en todos los formularios
- ✅ Hash de contraseñas automático
- ✅ Validación de permisos en backend (no solo frontend)
- ✅ Sesiones en base de datos
- ✅ LoginRequiredMixin + UserPassesTestMixin
- ✅ Redirecciones seguras a login
- ✅ Verificación de autenticidad en POST/PUT/DELETE

## FASE 9 ✅ - Perfil de Usuario

- ✅ **ProfileView** - Perfil del usuario autenticado
  - Requiere login (LoginRequiredMixin)
  - Muestra datos del usuario logueado
  - Últimos 6 juegos creados por el usuario
  - Últimas 6 reseñas del usuario
  - URL: `/usuarios/perfil/` → `users:profile`
  - Template: `users/profile.html`
  - Contexto: `profile_user`, `my_games`, `my_reviews`

- ✅ **MyGamesView** - Listado de mis juegos
  - Requiere login (LoginRequiredMixin)
  - Muestra solo los juegos creados por el usuario logueado
  - Ordenados por fecha de creación descendente
  - Paginación: 12 juegos por página
  - URL: `/usuarios/mis-juegos/` → `users:my_games`
  - Template: `users/my_games.html`
  - Contexto: `games`, paginación

- ✅ **MyReviewsView** - Listado de mis reseñas
  - Requiere login (LoginRequiredMixin)
  - Muestra solo las reseñas del usuario logueado
  - Ordenadas por fecha de creación descendente
  - Paginación: 12 reseñas por página
  - URL: `/usuarios/mis-resenas/` → `users:my_reviews`
  - Template: `users/my_reviews.html`
  - Contexto: `reviews`, paginación

- ✅ **Protección de datos:**
  - ProfileView solo accesible por el usuario autenticado
  - MyGamesView filtra por `created_by=request.user`
  - MyReviewsView filtra por `user=request.user`
- ✅ Otros usuarios no pueden ver perfil ajeno (filtrado en vista)

## FASE 10 ✅ - Templates (Navbar, Cards, Formularios)

**Estructura de Templates:**

```
templates/
├── base.html                      # Template base (navbar, footer, CSS)
├── games/
│   ├── game_list.html            # Listado de juegos con cards
│   ├── game_detail.html          # Detalle del juego + reseñas
│   ├── game_form.html            # Crear/Editar juego
│   └── game_confirm_delete.html  # Confirmar eliminar juego
├── reviews/
│   ├── review_form.html          # Crear/Editar reseña
│   └── review_confirm_delete.html # Confirmar eliminar reseña
└── users/
    ├── register.html             # Formulario de registro
    ├── login.html                # Formulario de login
    ├── profile.html              # Perfil del usuario
    ├── my_games.html             # Mis juegos (listado paginado)
    └── my_reviews.html           # Mis reseñas (listado paginado)
```

**Templates Creados:**

- ✅ **base.html** - Template base
  - Navbar con menú responsive (Bootstrap)
  - Footer
  - Mensajes de alerta
  - Estilos CSS básicos
  - Dropdown de usuario (cuando está logueado)

- ✅ **Games**:
  - `game_list.html`: Listado de juegos en cards, paginación 12/página
  - `game_detail.html`: Detalle completo + reseñas del juego
  - `game_form.html`: Formulario para crear/editar juego
  - `game_confirm_delete.html`: Confirmación de eliminar

- ✅ **Reviews**:
  - `review_form.html`: Formulario para crear/editar reseña (rating con radio buttons)
  - `review_confirm_delete.html`: Confirmación de eliminar

- ✅ **Users**:
  - `register.html`: Formulario de registro
  - `login.html`: Formulario de login con "remember me"
  - `profile.html`: Perfil con últimos 6 juegos + últimas 6 reseñas
  - `my_games.html`: Listado de mis juegos (paginado 12/página)
  - `my_reviews.html`: Listado de mis reseñas (paginado 12/página)

**Características de Templates:**

- ✅ Bootstrap 5 para estilos responsive
- ✅ Navbar adaptativo con menú hamburguesa
- ✅ Cards para juegos y reseñas
- ✅ Paginación en listados
- ✅ Formularios con error handling
- ✅ Condicionales para mostrar/ocultar botones (solo autor)
- ✅ Mensajes de alerta (info, warning, danger)
- ✅ Imágenes con fallback (placeholder si no hay imagen)
- ✅ Rating mostrado con estrellas (★)
- ✅ Timestamps formateados (d/m/Y H:i)

## FASE 11 ✅ - Funcionalidades Extras (Rating, Búsqueda, Paginación)

**Rating Promedio de Juegos:**

- ✅ **Método `get_average_rating()`** en Game model
  - Calcula rating promedio de todas las reseñas del juego
  - Devuelve 0 si no hay reseñas
  - Redondeado a 1 decimal
  - Usa `Avg()` de Django ORM

- ✅ **Método `get_review_count()`** en Game model
  - Devuelve número total de reseñas

- ✅ **Mostrado en**:
  - game_list.html: Rating con número de reseñas
  - game_detail.html: Rating promedio en tarjeta de información

**Buscador de Juegos:**

- ✅ **Campo de búsqueda** en game_list.html
  - Busca en: title, description, category
  - Case-insensitive (icontains)
  - Parámetro GET: `?search=...`

- ✅ **Lógica en GameListView**:
  ```python
  queryset.filter(
      Q(title__icontains=search_query) |
      Q(description__icontains=search_query) |
      Q(category__icontains=search_query)
  )
  ```

- ✅ **Características**:
  - Botón "Limpiar" para resetear búsqueda
  - Mensaje de resultados encontrados
  - Paginación mantiene parámetro de búsqueda

**Paginación:**

- ✅ **Ya implementada en todas las ListView**:
  - GameListView: 12 juegos/página
  - MyGamesView: 12 juegos/página
  - MyReviewsView: 12 reseñas/página

- ✅ **Controles de paginación**:
  - Primera/Anterior/Siguiente/Última
  - Página actual de total
  - Mantiene parámetros de búsqueda en URLs

**Métodos Simples Utilizados:**

- ✅ **Agregación**: `Avg()` para promedio
- ✅ **Filtrado**: `Q()` con OR para búsqueda múltiple
- ✅ **ORM**: `filter()`, `count()`, `aggregate()`
- ✅ **Templates**: Mostrar rating con condicionales simples
- ✅ **URLs**: Parámetros GET para búsqueda

## Actualizaciones Recientes ✅

**Sistema de Modo Claro/Oscuro con Tema y Cookies** (`templates/base.html`, `static/css/estilos.css`):

- ✅ Implementado sistema completo de cambio de tema (claro/oscuro)
- ✅ Preferencia guardada en cookie (365 días)
- ✅ Script JavaScript para cargar tema al iniciar
- ✅ Botón de toggle en la barra de navegación (opcional)
- ✅ Estilos personalizados para ambos modos:
  - Navbar, cards, formularios, alertas, dropdowns
  - Colores contrastantes y legibles en ambos modos
  - Gradientes de fondo diferentes para cada modo

**Traducción Completa del Formulario de Registro** (`users/forms.py`, `templates/users/register.html`):

- ✅ Etiquetas de campos en español:
  - "Nombre de usuario" (en lugar de "Username")
  - "Correo electrónico" (en lugar de "Email")
  - "Contraseña" (password1)
  - "Confirmar contraseña" (password2)

- ✅ Mensajes de ayuda en español:
  - Username: "Requerido. 150 caracteres o menos. Solo letras, números y @/./+/-/_"
  - Password: Lista de requisitos en español (8 caracteres, no común, etc.)
  - Confirmación de contraseña: "Por favor escribe la misma contraseña nuevamente."

**Visibilidad de Help Text en Modo Oscuro** (`static/css/estilos.css`, `templates/users/register.html`):

- ✅ Estilos CSS mejorados para help text:
  - Modo oscuro: Color blanco (#ffffff) para legibilidad
  - Modo claro: Color gris oscuro (#666) para contraste
  - Aplicado a `.form-text`, `small` y clase personalizada `.help-text-custom`
  
- ✅ HTML semántico:
  - Cambio de clase `text-muted` a `help-text-custom` en registro.html
  - Esto evita conflictos con estilos Bootstrap predeterminados
  - Estilos CSS con mayor especificidad para sobrescribir defaults

- ✅ Características:
  - Texto visible tanto en modo oscuro como claro
  - Incluye soporte para listas de HTML (ul/li) en help text
  - Aplicado a todos los campos del formulario de registro

## URLs y Vistas en Detalle

### GAMES - URLs disponibles

#### Listado de juegos
- **GET** `/juegos/` → `games:game_list`
- Vista: `GameListView`
- Paginación: 12 juegos por página

#### Detalle de juego
- **GET** `/juegos/game/<id>/` → `games:game_detail`
- Vista: `GameDetailView`
- Muestra detalles del juego e información del autor

#### Crear juego
- **GET/POST** `/juegos/crear/` → `games:game_create`
- Vista: `GameCreateView`
- Requiere login + asigna automáticamente `created_by`

#### Editar juego
- **GET/POST** `/juegos/game/<id>/editar/` → `games:game_update`
- Vista: `GameUpdateView`
- Requiere: login + ser el autor
- Si falla: redirige a detail

#### Eliminar juego
- **GET/POST** `/juegos/game/<id>/eliminar/` → `games:game_delete`
- Vista: `GameDeleteView`
- Requiere: login + ser el autor
- Si falla: redirige a detail

### REVIEWS - URLs disponibles

#### Crear reseña
- **GET/POST** `/resenas/juego/<game_id>/crear/` → `reviews:review_create`
- Vista: `ReviewCreateView`
- Requiere login + asigna automáticamente `game`, `user`
- Validación: unique_together (una reseña por usuario por juego)

#### Editar reseña
- **GET/POST** `/resenas/resena/<review_id>/editar/` → `reviews:review_update`
- Vista: `ReviewUpdateView`
- Requiere: login + ser el autor
- Si falla: redirige a detail del juego

#### Eliminar reseña
- **GET/POST** `/resenas/resena/<review_id>/eliminar/` → `reviews:review_delete`
- Vista: `ReviewDeleteView`
- Requiere: login + ser el autor
- Si falla: redirige a detail del juego

### USERS - URLs disponibles

#### Registro de usuario
- **GET/POST** `/usuarios/registro/` → `users:register`
- Vista: `RegisterView`
- Formulario: `RegisterForm`
- Campos: username, email, first_name, last_name, password1, password2
- Validación: email único + contraseña fuerte
- Redirección: Login

#### Inicio de sesión
- **GET/POST** `/usuarios/login/` → `users:login`
- Vista: `CustomLoginView`
- Formulario: `LoginForm` (con checkbox "remember me")
- Remember me: sesión persistente 30 días
- Redirección: GameListView

#### Cerrar sesión
- **GET** `/usuarios/logout/` → `users:logout`
- Vista: `CustomLogoutView`
- Redirección: GameListView

#### Perfil de usuario
- **GET** `/usuarios/perfil/` → `users:profile`
- Vista: `ProfileView`
- Requiere login
- Muestra: datos del usuario + últimos 6 juegos + últimas 6 reseñas
- Template: `users/profile.html`

#### Mis juegos
- **GET** `/usuarios/mis-juegos/` → `users:my_games`
- Vista: `MyGamesView`
- Requiere login
- Paginación: 12 juegos por página
- Filtra solo juegos del usuario autenticado
- Template: `users/my_games.html`

#### Mis reseñas
- **GET** `/usuarios/mis-resenas/` → `users:my_reviews`
- Vista: `MyReviewsView`
- Requiere login
- Paginación: 12 reseñas por página
- Filtra solo reseñas del usuario autenticado
- Template: `users/my_reviews.html`

### Ejemplos de uso en Templates

```django
{# GAMES - Enlaces #}
<a href="{% url 'games:game_list' %}">Ver todos los juegos</a>
<a href="{% url 'games:game_detail' game.pk %}">{{ game.title }}</a>
<a href="{% url 'games:game_create' %}">Crear juego</a>
<a href="{% url 'games:game_update' game.pk %}">Editar</a>
<a href="{% url 'games:game_delete' game.pk %}">Eliminar</a>

{# USERS - Verificar si está logueado #}
{% if user.is_authenticated %}
  <p>Hola, {{ user.username }}</p>
  <a href="{% url 'users:profile' %}">Mi perfil</a>
  <a href="{% url 'users:my_games' %}">Mis juegos</a>
  <a href="{% url 'users:my_reviews' %}">Mis reseñas</a>
  <a href="{% url 'users:logout' %}">Logout</a>
{% else %}
  <a href="{% url 'users:login' %}">Login</a>
  <a href="{% url 'users:register' %}">Registro</a>
{% endif %}

{# USERS - Acceso condicional (solo usuarios logueados) #}
{% if user.is_authenticated %}
  {# Contenido solo para usuarios logueados #}
{% else %}
  <p><a href="{% url 'users:login' %}">Inicia sesión</a> para acceder</p>
{% endif %}

{# REVIEWS - Crear reseña #}
{% if user.is_authenticated %}
  <a href="{% url 'reviews:review_create' game.pk %}">Escribe una reseña</a>
{% else %}
  <p>Inicia sesión para escribir una reseña</p>
{% endif %}

{# REVIEWS - Editar/Eliminar si es el autor #}
{% if review and review.user == user %}
  <a href="{% url 'reviews:review_update' review.pk %}">Editar mi reseña</a>
  <a href="{% url 'reviews:review_delete' review.pk %}">Eliminar mi reseña</a>
{% endif %}

{# REVIEWS - Mostrar todas las reseñas del juego #}
{% for review in game.reviews.all %}
  <div class="review">
    <strong>{{ review.user.username }}</strong>
    <span class="rating">{{ review.rating }}★</span>
    <p>{{ review.comment }}</p>
    {% if review.user == user %}
      <a href="{% url 'reviews:review_update' review.pk %}">Editar</a>
      <a href="{% url 'reviews:review_delete' review.pk %}">Eliminar</a>
    {% endif %}
  </div>
{% endfor %}

{# USERS - En perfil mostrar mis datos #}
<h2>{{ profile_user.username }}</h2>
<p>Email: {{ profile_user.email }}</p>
<p>Nombre: {{ profile_user.first_name }} {{ profile_user.last_name }}</p>

{# Últimos juegos en perfil #}
<h3>Mis últimos juegos (6)</h3>
{% for game in my_games %}
  <div class="game">
    <a href="{% url 'games:game_detail' game.pk %}">{{ game.title }}</a>
  </div>
{% empty %}
  <p>No has creado juegos aún</p>
{% endfor %}

{# Últimas reseñas en perfil #}
<h3>Mis últimas reseñas (6)</h3>
{% for review in my_reviews %}
  <div class="review">
    <strong>{{ review.game.title }}</strong>
    <span class="rating">{{ review.rating }}★</span>
    <p>{{ review.comment }}</p>
  </div>
{% empty %}
  <p>No has escrito reseñas aún</p>
{% endfor %}

{# GAMES - Paginación (en listado o mis-juegos) #}
{% if is_paginated %}
  <nav>
    {% if page_obj.has_previous %}
      <a href="?page=1">Primera</a>
      <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
    {% endif %}
    
    Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}
    
    {% if page_obj.has_next %}
      <a href="?page={{ page_obj.next_page_number }}">Siguiente</a>
      <a href="?page={{ page_obj.paginator.num_pages }}">Última</a>
    {% endif %}
  </nav>
{% endif %}
```

### Validaciones y Permisos

**LoginRequiredMixin:**
- Redirige a login si no está autenticado
- URL de login configurada en `settings.LOGIN_URL`

**UserPassesTestMixin:**
- Verifica que el usuario sea el autor (created_by o user)
- Si falla: `handle_no_permission()` redirige a detail

**unique_together (game, user) en Review:**
- Un usuario solo puede tener 1 reseña por juego
- Si intenta crear otra → IntegrityError → mensaje en formulario
- Para modificarla → usar vista de edición

## Configuración actual

### Base de datos (Desarrollo local)
- Motor: SQLite
- Archivo: `db.sqlite3`
- Estado: ✅ Migraciones aplicadas

### Ambiente
- DEBUG: True
- SECRET_KEY: Configurada en .env
- ALLOWED_HOSTS: localhost, 127.0.0.1, web

## Notas
- **Desarrollo local**: Usa SQLite (sin dependencias externas)
- **Docker**: Cambia automáticamente a PostgreSQL (ver docker-compose.yml)
- Tabla de migraciones: ✅ Contenidas en auth, admin, sessions
- Media storage: Listo para cargar imágenes de juegos

## Comandos útiles (Desarrollo local)

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

python manage.py startapp nombre_app
```

## Admin de Django - Configuración Completa ✅

**GameAdmin** (`games/admin.py`):

- ✅ **Listado personalizado con colores**:
  - Título con badge de color según categoría
  - Categoría con badge de color
  - Rating con estrellas (⭐)
  - Número de reseñas con indicador de color

- ✅ **Filtros avanzados**: Por categoría, fecha de creación, fecha de lanzamiento

- ✅ **Búsqueda**: Por título, descripción, username del autor

- ✅ **Fieldsets organizados**:
  - 📌 Información Básica
  - 🎨 Multimedia (con preview de imagen)
  - 📅 Detalles
  - ⭐ Estadísticas (rating calculado)
  - 🕐 Registro (colapsable)

- ✅ **Acciones personalizadas**:
  - ⭐ Marcar como destacado
  - 🗑️ Eliminar imagen de juegos

- ✅ **Funciones especiales**: `image_preview()`, `rating_display()`, `reviews_count()`, `title_colored()`

**ReviewAdmin** (`reviews/admin.py`):

- ✅ **Listado personalizado**:
  - Usuario con link directo
  - Juego con link directo
  - Rating con estrellas coloreadas (rojo/amarillo/verde)
  - Preview del comentario

- ✅ **Filtros avanzados**: Por rating, fecha, juego, usuario

- ✅ **Búsqueda**: Por username, juego, comentario

- ✅ **Fieldsets organizados**:
  - 👤 Autor y Juego
  - ⭐ Calificación
  - 💬 Comentario
  - 🕐 Registro (colapsable)

- ✅ **Acciones personalizadas**:
  - ✅ Aprobar reseña
  - 😊 Mostrar positivas (4-5★)
  - 😞 Mostrar negativas (1-2★)

- ✅ **Funciones especiales**: `rating_stars()`, `comment_formatted()`, `user_link()`, `game_link()`

**CustomUserAdmin** (`users/admin.py`):

- ✅ **Listado personalizado**:
  - Username con prefijo 👑 si es staff
  - Email con link mailto
  - Número de juegos creados
  - Número de reseñas escritas
  - Indicador de staff
  - Último login formateado

- ✅ **Inlines**:
  - Juegos creados por el usuario (read-only)
  - Reseñas escritas por el usuario (read-only)

- ✅ **Filtros**: Por activo, staff, fecha de registro, último login

- ✅ **Búsqueda**: Por username, email, nombre, apellido

- ✅ **Estadísticas**:
  - Número de juegos con rating promedio
  - Número de reseñas con rating promedio

- ✅ **Funciones especiales**: `username_colored()`, `email_display()`, `games_stats()`, `reviews_stats()`

**Características Generales:**

- ✅ Colores personalizados para estados
- ✅ Iconos emoji para visualización
- ✅ Links internos entre modelos
- ✅ Date hierarchy para navegación
- ✅ Acciones en lote (bulk actions)
- ✅ Readonly fields para datos calculados
- ✅ Fieldsets colapsables
- ✅ Format HTML para estilos avanzados

## Próximas fases

- **FASE 3**: ✅ Modelos (Game, Review)
- **FASE 4**: ✅ Formularios (GameForm, ReviewForm)
- **FASE 5**: ✅ Vistas CRUD (List, Detail, Create, Edit, Delete)
- **FASE 6**: ✅ Reseñas (Create, Edit, Delete)
- **FASE 7**: ✅ Sistema de usuarios (Registro, Login, Logout, Remember Me)
- **FASE 8**: ✅ Permisos básicos (LoginRequired, UserPassesTest)
- **FASE 9**: ✅ Perfil de usuario (Perfil, Mis juegos, Mis reseñas)
- **FASE 10**: ✅ Templates (Navbar, Cards, Formularios)
- **FASE 11**: ✅ Funcionalidades extras (Rating, Búsqueda, Paginación)
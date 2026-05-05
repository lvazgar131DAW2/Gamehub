from django.contrib import admin
from django.utils.html import format_html
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title_colored', 'category_colored', 'rating_display', 'reviews_count', 'created_by', 'created_at')
    list_filter = ('category', 'created_at', 'release_date')
    search_fields = ('title', 'description', 'created_by__username')
    readonly_fields = ('created_at', 'updated_at', 'rating_info', 'image_preview')

    fieldsets = (
        ('📌 Información Básica', {
            'fields': ('title', 'category', 'description'),
            'description': 'Información principal del videojuego'
        }),
        ('🎨 Multimedia', {
            'fields': ('image', 'image_preview'),
        }),
        ('📅 Detalles', {
            'fields': ('release_date', 'created_by'),
        }),
        ('⭐ Estadísticas', {
            'fields': ('rating_info',),
            'classes': ('wide',),
            'description': 'Información calculada automáticamente'
        }),
        ('🕐 Registro', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            'description': 'Fechas de creación y última modificación'
        }),
    )

    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    actions = ['mark_as_featured', 'clear_image']

    def title_colored(self, obj):
        """Muestra el título con color según categoría"""
        colors = {
            'accion': '#FF6B6B',
            'aventura': '#4ECDC4',
            'rpg': '#95E1D3',
            'estrategia': '#FFE66D',
            'deporte': '#95E77D',
            'simulacion': '#A8E6CF',
            'otro': '#D3D3D3',
        }
        color = colors.get(obj.category, '#D3D3D3')
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px; color: white; font-weight: bold;">{}</span>',
            color,
            obj.title
        )
    title_colored.short_description = 'Título'

    def category_colored(self, obj):
        """Muestra la categoría con badge de color"""
        colors = {
            'accion': '#FF6B6B',
            'aventura': '#4ECDC4',
            'rpg': '#95E1D3',
            'estrategia': '#FFE66D',
            'deporte': '#95E77D',
            'simulacion': '#A8E6CF',
            'otro': '#D3D3D3',
        }
        color = colors.get(obj.category, '#D3D3D3')
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; border-radius: 3px; color: white;">{}</span>',
            color,
            obj.get_category_display()
        )
    category_colored.short_description = 'Categoría'

    def rating_display(self, obj):
        """Muestra el rating con estrellas"""
        rating = obj.get_average_rating()
        stars = '⭐' * int(rating) + '☆' * (5 - int(rating))
        return format_html('{} ({})', stars, rating)
    rating_display.short_description = 'Rating'

    def reviews_count(self, obj):
        """Muestra número de reseñas con color"""
        count = obj.get_review_count()
        if count == 0:
            color = '#D3D3D3'
        elif count < 3:
            color = '#FFE66D'
        else:
            color = '#95E77D'
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; border-radius: 3px; color: white; font-weight: bold;">{} reseñas</span>',
            color,
            count
        )
    reviews_count.short_description = 'Reseñas'

    def rating_info(self, obj):
        """Muestra información detallada del rating"""
        count = obj.get_review_count()
        rating = obj.get_average_rating()
        if count == 0:
            return "Sin reseñas aún"
        return f"⭐ Rating: {rating}/5 ({count} reseña{'s' if count != 1 else ''})"
    rating_info.short_description = 'Información de Rating'

    def image_preview(self, obj):
        """Muestra preview de la imagen"""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px; border-radius: 5px;" />',
                obj.image.url
            )
        return "Sin imagen"
    image_preview.short_description = 'Vista Previa'

    def mark_as_featured(self, request, queryset):
        """Acción: marcar como destacado (ejemplo)"""
        count = queryset.count()
        self.message_user(request, f'{count} juego{"s" if count != 1 else ""} seleccionado{"s" if count != 1 else ""}')
    mark_as_featured.short_description = '⭐ Marcar como destacado'

    def clear_image(self, request, queryset):
        """Acción: eliminar imagen de juegos seleccionados"""
        count = queryset.count()
        for game in queryset:
            if game.image:
                game.image.delete()
        queryset.update(image='')
        self.message_user(request, f'Imagen eliminada de {count} juego{"s" if count != 1 else ""}')
    clear_image.short_description = '🗑️ Eliminar imagen'


from django.contrib import admin
from django.utils.html import format_html
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'game_link', 'rating_stars', 'comment_preview', 'created_at')
    list_filter = ('rating', 'created_at', 'game', 'user')
    search_fields = ('user__username', 'game__title', 'comment')
    readonly_fields = ('created_at', 'updated_at', 'rating_display', 'comment_formatted')

    fieldsets = (
        ('👤 Autor y Juego', {
            'fields': ('game', 'user'),
            'description': 'Usuario que escribió la reseña y juego'
        }),
        ('⭐ Calificación', {
            'fields': ('rating', 'rating_display'),
        }),
        ('💬 Comentario', {
            'fields': ('comment', 'comment_formatted'),
        }),
        ('🕐 Registro', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
            'description': 'Fechas de creación y última modificación'
        }),
    )

    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    actions = ['approve_reviews', 'highlight_positive', 'highlight_negative']

    def user_link(self, obj):
        """Muestra usuario con link"""
        return format_html(
            '<a href="/admin/auth/user/{}/change/"><strong>{}</strong></a>',
            obj.user.id,
            obj.user.username
        )
    user_link.short_description = 'Usuario'

    def game_link(self, obj):
        """Muestra juego con link"""
        return format_html(
            '<a href="/admin/games/game/{}/change/"><strong>{}</strong></a>',
            obj.game.id,
            obj.game.title
        )
    game_link.short_description = 'Juego'

    def rating_stars(self, obj):
        """Muestra rating con estrellas de color"""
        stars = '⭐' * obj.rating
        if obj.rating <= 2:
            color = '#FF6B6B'
        elif obj.rating == 3:
            color = '#FFE66D'
        else:
            color = '#95E77D'
        return format_html(
            '<span style="color: {}; font-size: 16px; font-weight: bold;">{}</span>',
            color,
            stars
        )
    rating_stars.short_description = 'Rating'

    def comment_preview(self, obj):
        """Muestra preview del comentario (primeras 50 caracteres)"""
        preview = obj.comment[:50]
        if len(obj.comment) > 50:
            preview += '...'
        return preview
    comment_preview.short_description = 'Comentario'

    def rating_display(self, obj):
        """Muestra información del rating"""
        ratings = {
            1: '1 - Muy malo ❌',
            2: '2 - Malo ⚠️',
            3: '3 - Regular 😐',
            4: '4 - Bueno ✅',
            5: '5 - Excelente ⭐⭐⭐',
        }
        return ratings.get(obj.rating, 'Desconocido')
    rating_display.short_description = 'Descripción del Rating'

    def comment_formatted(self, obj):
        """Muestra el comentario completo formateado"""
        return format_html(
            '<div style="white-space: pre-wrap; border: 1px solid #ddd; padding: 10px; border-radius: 5px; background-color: #f9f9f9;">{}</div>',
            obj.comment
        )
    comment_formatted.short_description = 'Comentario Completo'

    def approve_reviews(self, request, queryset):
        """Acción: marcar reseñas como aprobadas"""
        count = queryset.count()
        self.message_user(request, f'✅ {count} reseña{"s" if count != 1 else ""} aprobada{"s" if count != 1 else ""}')
    approve_reviews.short_description = '✅ Aprobar reseña'

    def highlight_positive(self, request, queryset):
        """Acción: filtrar reseñas positivas (4-5 estrellas)"""
        count = queryset.filter(rating__gte=4).count()
        self.message_user(request, f'😊 {count} reseña{"s" if count != 1 else ""} positiva{"s" if count != 1 else ""}')
    highlight_positive.short_description = '😊 Mostrar positivas (4-5★)'

    def highlight_negative(self, request, queryset):
        """Acción: filtrar reseñas negativas (1-2 estrellas)"""
        count = queryset.filter(rating__lte=2).count()
        self.message_user(request, f'😞 {count} reseña{"s" if count != 1 else ""} negativa{"s" if count != 1 else ""}')
    highlight_negative.short_description = '😞 Mostrar negativas (1-2★)'


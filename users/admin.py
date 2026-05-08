from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from games.models import Game
from reviews.models import Review


admin.site.unregister(User)


class UserGameInline(admin.TabularInline):
    model = Game
    extra = 0
    fields = ('title', 'category', 'created_at')
    readonly_fields = ('title', 'category', 'created_at')
    can_delete = False


class UserReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    fields = ('game', 'rating', 'created_at')
    readonly_fields = ('game', 'rating', 'created_at')
    can_delete = False


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserGameInline, UserReviewInline)

    list_display = ('username_colored', 'email_display', 'games_count', 'reviews_count', 'is_staff_display', 'last_login_display')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('📊 Estadísticas', {
            'fields': ('games_stats', 'reviews_stats'),
            'description': 'Información sobre contenido del usuario'
        }),
    )
    readonly_fields = BaseUserAdmin.readonly_fields + ('games_stats', 'reviews_stats')

    def username_colored(self, obj):
        if obj.is_staff:
            color = '#FFE66D'
            prefix = '👑 '
        else:
            color = '#95E77D'
            prefix = '👤 '
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px; color: white; font-weight: bold;">{}{}</span>',
            color,
            prefix,
            obj.username
        )
    username_colored.short_description = 'Usuario'

    def email_display(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email,
            obj.email if obj.email else 'Sin email'
        )
    email_display.short_description = 'Email'

    def games_count(self, obj):
        count = obj.games.count()
        if count == 0:
            color = '#D3D3D3'
        elif count < 3:
            color = '#FFE66D'
        else:
            color = '#95E77D'
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; border-radius: 3px; color: white; font-weight: bold;">{} 🎮</span>',
            color,
            count
        )
    games_count.short_description = 'Juegos'

    def reviews_count(self, obj):
        count = obj.reviews.count()
        if count == 0:
            color = '#D3D3D3'
        elif count < 5:
            color = '#FFE66D'
        else:
            color = '#4ECDC4'
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; border-radius: 3px; color: white; font-weight: bold;">{} 💬</span>',
            color,
            count
        )
    reviews_count.short_description = 'Reseñas'

    def is_staff_display(self, obj):
        if obj.is_staff:
            return format_html('<span style="color: #FFE66D; font-size: 18px;">👑</span>')
        return format_html('<span style="color: #D3D3D3;">-</span>')
    is_staff_display.short_description = 'Staff'

    def last_login_display(self, obj):
        if obj.last_login:
            return obj.last_login.strftime('%d/%m/%Y %H:%M')
        return 'Nunca'
    last_login_display.short_description = 'Último Login'

    def games_stats(self, obj):
        count = obj.games.count()
        if count == 0:
            return 'Sin juegos creados'
        avg_rating = sum([g.get_average_rating() for g in obj.games.all()]) / count
        return format_html(
            '<strong>{} juego{"s" if count != 1 else ""}</strong> • Rating promedio: <strong>{:.1f}★</strong>',
            count,
            avg_rating
        )
    games_stats.short_description = 'Juegos Creados'

    def reviews_stats(self, obj):
        count = obj.reviews.count()
        if count == 0:
            return 'Sin reseñas escritas'
        avg_rating = sum([r.rating for r in obj.reviews.all()]) / count
        return format_html(
            '<strong>{} reseña{"s" if count != 1 else ""}</strong> • Rating promedio: <strong>{:.1f}★</strong>',
            count,
            avg_rating
        )
    reviews_stats.short_description = 'Reseñas Escritas'
    inlines = (UserGameInline, UserReviewInline)

    list_display = ('username_colored', 'email_display', 'games_count', 'reviews_count', 'is_staff_display', 'last_login_display')
    list_filter = ('is_active', 'is_staff', 'date_joined', 'last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('📊 Estadísticas', {
            'fields': ('games_stats', 'reviews_stats'),
            'description': 'Información sobre contenido del usuario'
        }),
    )
    readonly_fields = BaseUserAdmin.readonly_fields + ('games_stats', 'reviews_stats')

    def username_colored(self, obj):
        if obj.is_staff:
            color = '#FFE66D'
            prefix = '👑 '
        else:
            color = '#95E77D'
            prefix = '👤 '
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px; color: white; font-weight: bold;">{}{}</span>',
            color,
            prefix,
            obj.username
        )
    username_colored.short_description = 'Usuario'

    def email_display(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email,
            obj.email if obj.email else 'Sin email'
        )
    email_display.short_description = 'Email'

    def games_count(self, obj):
        count = obj.games.count()
        if count == 0:
            color = '#D3D3D3'
        elif count < 3:
            color = '#FFE66D'
        else:
            color = '#95E77D'
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; border-radius: 3px; color: white; font-weight: bold;">{} 🎮</span>',
            color,
            count
        )
    games_count.short_description = 'Juegos'

    def reviews_count(self, obj):
        count = obj.reviews.count()
        if count == 0:
            color = '#D3D3D3'
        elif count < 5:
            color = '#FFE66D'
        else:
            color = '#4ECDC4'
        return format_html(
            '<span style="background-color: {}; padding: 3px 8px; border-radius: 3px; color: white; font-weight: bold;">{} 💬</span>',
            color,
            count
        )
    reviews_count.short_description = 'Reseñas'

    def is_staff_display(self, obj):
        if obj.is_staff:
            return format_html('<span style="color: #FFE66D; font-size: 18px;">👑</span>')
        return format_html('<span style="color: #D3D3D3;">-</span>')
    is_staff_display.short_description = 'Staff'

    def last_login_display(self, obj):
        if obj.last_login:
            return obj.last_login.strftime('%d/%m/%Y %H:%M')
        return 'Nunca'
    last_login_display.short_description = 'Último Login'

    def games_stats(self, obj):
        count = obj.games.count()
        if count == 0:
            return 'Sin juegos creados'
        avg_rating = sum([g.get_average_rating() for g in obj.games.all()]) / count
        return format_html(
            '<strong>{} juego{"s" if count != 1 else ""}</strong> • Rating promedio: <strong>{:.1f}★</strong>',
            count,
            avg_rating
        )
    games_stats.short_description = 'Juegos Creados'

    def reviews_stats(self, obj):
        count = obj.reviews.count()
        if count == 0:
            return 'Sin reseñas escritas'
        avg_rating = sum([r.rating for r in obj.reviews.all()]) / count
        return format_html(
            '<strong>{} reseña{"s" if count != 1 else ""}</strong> • Rating promedio: <strong>{:.1f}★</strong>',
            count,
            avg_rating
        )
    reviews_stats.short_description = 'Reseñas Escritas'



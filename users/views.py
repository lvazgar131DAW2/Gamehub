from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from games.models import Game
from reviews.models import Review
from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('games:game_list')

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        user = form.get_user()

        login(self.request, user)

        if remember_me:
            self.request.session.set_expiry(30 * 24 * 60 * 60)
        else:
            self.request.session.set_expiry(0)

        return redirect(self.get_success_url())


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('games:game_list')


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_games'] = self.request.user.games.all()[:6]
        context['my_reviews'] = self.request.user.reviews.all()[:6]
        return context


class MyGamesView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'users/my_games.html'
    context_object_name = 'games'
    paginate_by = 12

    def get_queryset(self):
        return Game.objects.filter(created_by=self.request.user).order_by('-created_at')


class MyReviewsView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'users/my_reviews.html'
    context_object_name = 'reviews'
    paginate_by = 12

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-created_at')


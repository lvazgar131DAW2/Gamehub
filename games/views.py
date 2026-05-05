from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Game
from .forms import GameForm


class GameListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'
    paginate_by = 12

    def get_queryset(self):
        queryset = Game.objects.all()
        search_query = self.request.GET.get('search', '')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(category__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    context_object_name = 'game'


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game_form.html'
    success_url = reverse_lazy('games:game_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game_form.html'
    success_url = reverse_lazy('games:game_list')

    def test_func(self):
        game = self.get_object()
        return self.request.user == game.created_by

    def handle_no_permission(self):
        return redirect('games:game_detail', pk=self.get_object().pk)


class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    template_name = 'games/game_confirm_delete.html'
    success_url = reverse_lazy('games:game_list')

    def test_func(self):
        game = self.get_object()
        return self.request.user == game.created_by

    def handle_no_permission(self):
        return redirect('games:game_detail', pk=self.get_object().pk)

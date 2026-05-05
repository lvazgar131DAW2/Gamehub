from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db import IntegrityError
from games.models import Game
from .models import Review
from .forms import ReviewForm


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.game = get_object_or_404(Game, pk=kwargs['game_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.game
        return context

    def form_valid(self, form):
        form.instance.game = self.game
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error(None, 'Ya has creado una reseña para este juego. Edítala en su lugar.')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('games:game_detail', kwargs={'pk': self.game.pk})


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.get_object().game
        return context

    def handle_no_permission(self):
        review = self.get_object()
        return redirect('games:game_detail', pk=review.game.pk)

    def get_success_url(self):
        review = self.get_object()
        return reverse_lazy('games:game_detail', kwargs={'pk': review.game.pk})


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.get_object().game
        return context

    def handle_no_permission(self):
        review = self.get_object()
        return redirect('games:game_detail', pk=review.game.pk)

    def get_success_url(self):
        review = self.get_object()
        return reverse_lazy('games:game_detail', kwargs={'pk': review.game.pk})

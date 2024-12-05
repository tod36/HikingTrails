from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import CommentForm, TrailPhotosForm, TrailForm
from .models import Comment
from .models import Trails
from ..Hikers.models import Hiker


class TrailsCreateView(CreateView):
    model = Trails
    template_name = 'trails/trail_create.html'
    fields = ['name', 'length', 'image', 'difficulty', 'description', 'elevation_gain', 'hiker']
    success_url = reverse_lazy('trail_list')


class TrailsListView(ListView):
    model = Trails
    template_name = 'trails/trail_list.html'
    context_object_name = 'trails'


class TrailsDetailView(DetailView):
    model = Trails
    template_name = 'trails/trail_details.html'
    context_object_name = 'trail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(trail=self.object)
        paginator = Paginator(comments, 5)  # Show 5 comments per page
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['form'] = CommentForm()
        context['photo_form'] = TrailPhotosForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'comment' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.trail = self.object
                comment.user = request.user
                comment.save()
        elif 'photo' in request.POST:
            photo_form = TrailPhotosForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                photo.trail = self.object
                photo.save()
        return redirect('trail_details', pk=self.object.pk)


class TrailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trails
    success_url = reverse_lazy('trail_list')  # Replace with your trail list view name

    def test_func(self):
        trail = self.get_object()
        return self.request.user == trail.hiker and self.request.user.is_approved


class TrailEditView(UpdateView):
    model = Trails
    form_class = TrailForm
    template_name = 'trails/trail_edit.html'

    def form_valid(self, form):
        trail = form.save(commit=False)
        trail.save()
        return redirect('trail_details', pk=trail.pk)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'trails/comment_trail.html'
    fields = ['text']
    success_url = reverse_lazy('trail_list')

    def form_valid(self, form):
        user = self.request.user
        if not Hiker.objects.filter(id=user.id).exists():
            return HttpResponseForbidden("User does not exist.")
        form.instance.user = user
        form.instance.trail_id = self.kwargs['pk']
        if user.is_authenticated:
            return super().form_valid(form)
        else:
            return self.handle_no_permission()


def custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

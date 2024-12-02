from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .models import Comment
from .models import Trails
from ..Hikers.models import Hiker


class TrailsCreateView(CreateView):
    model = Trails
    template_name = 'trails/trails_create.html'
    fields = ['name', 'length', 'image', 'difficulty', 'description', 'elevation_gain', 'hiker']
    success_url = reverse_lazy('trail_list')


class TrailsListView(ListView):
    model = Trails
    template_name = 'trails/trail_list.html'
    context_object_name = 'trails'


class TrailsDetailView(DetailView):
    model = Trails
    template_name = 'trails/trails_detail.html'
    context_object_name = 'trail'


class TrailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trails
    success_url = reverse_lazy('trail_list')  # Replace with your trail list view name

    def test_func(self):
        trail = self.get_object()
        return self.request.user == trail.hiker and self.request.user.is_approved

# def create_comment(request):
#     hiker = Hiker.objects.get(id=request.POST['hiker_id'])
#     comment = Comment(comment=request.POST['comment'], hiker_id=hiker)
#     comment.save()



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
        if user.is_approved:
            return super().form_valid(form)
        else:
            return self.handle_no_permission()

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.trail_id = self.kwargs['pk']
    #     if self.request.user.is_approved:
    #         return super().form_valid(form)
    #     else:
    #         return self.handle_no_permission()


# def get_form(self, form_class=None):
#     form = super().get_form(form_class)
#     form.fields['user'].disabled = True
#     return form

# def form_valid(self, form):
#     form.instance.user = self.request.user
#     form.instance.trail_id = self.kwargs['pk']
#     if not self.request.user.is_approved:
#         return self.handle_no_permission()
#     return super().form_valid(form)


def custom_permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

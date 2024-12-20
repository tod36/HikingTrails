from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.views.generic import ListView

from .forms import MeetingForm, MeetingPhotosForm
from .models import Meeting, MeetingPhotos


class MeetingListView(ListView):
    model = MeetingPhotos
    template_name = 'academy/photo_list.html'
    context_object_name = 'photos_by_year'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = MeetingPhotos.objects.all().order_by('meeting')
        photos_by_year = {}
        for photo in photos:
            year = photo.meeting
            if year not in photos_by_year:
                photos_by_year[year] = []
            photos_by_year[year].append(photo)
        context['photos_by_year'] = photos_by_year
        return context


class MeetingCreateView(CreateView):
    model = Meeting
    form_class = MeetingForm
    template_name = 'academy/meeting_form.html'
    success_url = reverse_lazy('photo_list')


class MeetingPhotosView(CreateView):
    model = MeetingPhotos
    form_class = MeetingPhotosForm
    template_name = 'academy/upload_photo.html'
    success_url = reverse_lazy('photo_list')

# class MeetingUpdateView(UpdateView):
#     model = Meeting
#     form_class = MeetingForm
#     template_name = 'academy/meeting_form.html'
#     success_url = reverse_lazy('meeting_list')
#
#
class MeetingPhotosDeleteView(DeleteView):
    model = MeetingPhotos
    template_name = 'academy/confirm_delete.html'
    success_url = reverse_lazy('photo_list')

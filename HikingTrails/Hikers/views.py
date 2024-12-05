from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from HikingTrails.Hikers.forms import HikerRegForm, HikerDetailForm
from HikingTrails.Hikers.models import Hiker


class HikerRegView(View):
    form_class = HikerRegForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_with_nav')
        return render(request, self.template_name, {'form': form})


class HikerDetailView(View):
    form_class = HikerRegForm
    initial = {'key': 'value'}
    template_name = 'hikers/hiker_details.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_with_nav')
        return render(request, self.template_name, {'form': form})


class HikerUpdateView(View):
    form_class = HikerDetailForm
    exclude = ['username', 'email']
    template_name = 'hikers/hiker_update.html'

    def get(self, request, *args, **kwargs):
        hiker = Hiker.objects.get(pk=kwargs['pk'])
        form = self.form_class(instance=hiker)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        hiker = Hiker.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST, request.FILES, instance=hiker)
        if form.is_valid():
            form.save()
            return redirect('home_with_nav')
        return render(request, self.template_name, {'form': form})


class HikerDeleteView(View):
    template_name = 'hikers/hiker_delete.html'

    def get(self, request, *args, **kwargs):
        hiker = Hiker.objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, {'hiker': hiker})

    def post(self, request, *args, **kwargs):
        hiker = Hiker.objects.get(pk=kwargs['pk'])
        hiker.delete()
        return redirect('home_with_nav')


def home(request):
    return render(request, 'home.html')


def home_with_nav(request):
    return render(request, 'hikers/home_with_nav.html')


def approved_hikers(request):
    approved_hikers_list = Hiker.objects.filter(is_approved=True)
    return render(request, 'hikers/approved_hikers.html', {'approved_hikers': approved_hikers_list})

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from HikingTrails.Hikers.forms import HikerRegForm


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


def home(request):
    return render(request, 'home.html')


def home_with_nav(request):
    return render(request, 'hikers/home_with_nav.html')


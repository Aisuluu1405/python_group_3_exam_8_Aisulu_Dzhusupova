from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from webapp.models import Services


class IndexView(ListView):
    model = Services
    template_name = 'service/index.html'
    context_object_name = 'services_list'


class ServicesView(DetailView):
    model = Services
    template_name = 'service/detail.html'
    context_object_name = 'services'


class ServicesCreateView(CreateView):
    model = Services
    template_name = 'service/create.html'
    fields = ('name', 'category', 'description', 'photo')
    success_url = reverse_lazy('webapp:index')
    # permission_required = 'webapp.add_services'
    # permission_denied_message = "Доступ запрещен"

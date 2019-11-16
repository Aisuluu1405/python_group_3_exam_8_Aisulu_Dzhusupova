from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


class ServicesEditView(UpdateView):
    template_name = 'service/edit.html'
    model = Services
    fields = ('name', 'category', 'description', 'photo')
    context_object_name = 'services'

    def get_success_url(self):
        return reverse('webapp:index')

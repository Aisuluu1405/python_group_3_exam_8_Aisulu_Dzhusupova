from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ServiceReviewForm
from webapp.models import Services


class IndexView(ListView):
    model = Services
    template_name = 'service/index.html'
    context_object_name = 'services_list'


class ServicesView(DetailView):
    model = Services
    template_name = 'service/detail.html'
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ServiceReviewForm
        service_review = context['services'].service_review.order_by('-rating')
        self.paginate_reviews_to_context(service_review, context)
        return context

    def paginate_reviews_to_context(self, reviews, context):
        paginator = Paginator(reviews, 5, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['reviews'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


class ServicesCreateView(PermissionRequiredMixin, CreateView):
    model = Services
    template_name = 'service/create.html'
    fields = ('name', 'category', 'description', 'photo')
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.add_services'
    permission_denied_message = "Доступ запрещен!"


class ServicesEditView(PermissionRequiredMixin, UpdateView):
    template_name = 'service/edit.html'
    model = Services
    fields = ('name', 'category', 'description', 'photo')
    context_object_name = 'services'
    permission_required = 'webapp.change_services'
    permission_denied_message = "Доступ запрещен!"

    def get_success_url(self):
        return reverse('webapp:index')


class ServicesDeleteView(PermissionRequiredMixin, DeleteView):
    model = Services
    template_name = 'service/delete.html'
    context_object_name = 'services'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_services'
    permission_denied_message = 'Доступ запрещен!'


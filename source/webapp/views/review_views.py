from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import  get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from webapp.forms import ServiceReviewForm
from webapp.models import Review, Services


class ReviewForServiceCreateView(CreateView):
    template_name = 'review/create.html'
    form_class = ServiceReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Services.objects.get(pk=self.kwargs['pk'])
        context['services'] = services
        return context

    def form_valid(self, form):
        services_pk = self.kwargs.get('pk')
        services = get_object_or_404(Services, pk=services_pk)
        services.service_review.create(author=self.request.user, **form.cleaned_data)
        return redirect('webapp:service_detail', pk=services_pk)


class ReviewEditView(UpdateView):
    model = Review
    template_name = 'review/edit.html'
    form_class = ServiceReviewForm
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('webapp:service_detail', kwargs={'pk': self.object.service.pk})


class ReviewDeleteView(DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:service_detail', kwargs={'pk': self.object.service.pk})
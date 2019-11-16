from django.urls import path
from webapp.views.service_views import IndexView, ServicesView, ServicesCreateView, ServicesEditView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/<int:pk>', ServicesView.as_view(), name='service_detail'),
    path('services/create', ServicesCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/edit/', ServicesEditView.as_view(), name='service_edit'),
#
]

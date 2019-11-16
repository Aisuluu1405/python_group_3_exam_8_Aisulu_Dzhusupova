from django.urls import path
from webapp.views.service_views import IndexView, ServicesView, ServicesCreateView, ServicesEditView, ServicesDeleteView
from webapp.views.review_views import ReviewForServiceCreateView, ReviewEditView, ReviewDeleteView


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('services/<int:pk>', ServicesView.as_view(), name='service_detail'),
    path('services/create', ServicesCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/edit/', ServicesEditView.as_view(), name='service_edit'),
    path('services/delete/<int:pk>/', ServicesDeleteView.as_view(), name='service_delete'),
    path('services/<int:pk>/add-review/', ReviewForServiceCreateView.as_view(), name='review_create'),
    path('comment/<int:pk>/edit/', ReviewEditView.as_view(), name='review_update'),
    path('comment/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),

    # path('review/create', ReviewForServiceCreateView.as_view(), name='review_create')

#
]

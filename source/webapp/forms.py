from django import forms
from webapp.models import Review


class ServiceReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
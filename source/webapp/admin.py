from django.contrib import admin
from webapp.models import Services, Review


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description']
    list_filter = ['name']
    search_fields = ['name', 'category']
    exclude = []


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'service', 'rating']
    list_filter = ['author']
    search_fields = ['service']
    exclude = []


admin.site.register(Services, ServiceAdmin)
admin.site.register(Review, ReviewAdmin)

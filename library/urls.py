from django.urls import path

from .views import csv_upload_view, UploadTemplateView, home_view

app_name = 'library'

urlpatterns = [
    path('', home_view, name='home'),
    path('?sort=date', home_view, name='home_order'),
    path('from_file/', UploadTemplateView.as_view(), name='from-file'),
    path('upload/', csv_upload_view, name='upload'),
]

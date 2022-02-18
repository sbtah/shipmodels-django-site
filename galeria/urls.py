from django.urls import path
from galeria import views

app_name = 'galeria'

urlpatterns = [
    path('', views.ImagePostListView.as_view(), name='image-list'),
]

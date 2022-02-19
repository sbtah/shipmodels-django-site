from django.urls import path
from galeria import views

app_name = 'galeria'

urlpatterns = [
    path('gallery/', views.ImageGalleryListView.as_view(), name='gallery-list'),
    path('image-list/', views.ImagePostListView.as_view(), name='image-list'),
]

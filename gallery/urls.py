from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    # Galleries
    path('', views.ImageGalleryListView.as_view(), name='gallery-list'),
    path('images/', views.ImagePostListView.as_view(), name='image-list'),
    path('<str:slug>/',
         views.ImageGalleryDetailView.as_view(), name='gallery-detail'),
    path('image/<str:slug>/',
         views.ImagePostDetailView.as_view(), name='image-detail'),
]

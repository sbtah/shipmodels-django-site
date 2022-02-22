from django.urls import path
from gallery import views

app_name = 'gallery'

urlpatterns = [
    path('', views.ImageGalleryListView.as_view(), name='gallery-list'),
    path('image-detail/<str:slug>/',
         views.ImagePostDetailView.as_view(), name='image-detail'),
    path('image-list/', views.ImagePostListView.as_view(), name='image-list'),
]

from django.urls import path
from gallery import views
from django.utils.translation import gettext_lazy as _


app_name = 'gallery'


urlpatterns = [
    # Galleries
    path('', views.ImageGalleryListView.as_view(), name='gallery-list'),
    path(_('obrazy/'), views.ImagePostListView.as_view(), name='image-list'),
    path(_('<str:slug>/'),
         views.ImageGalleryDetailView.as_view(), name='gallery-detail'),
    path(_('obraz/<str:slug>/'),
         views.ImagePostDetailView.as_view(), name='image-detail'),
]

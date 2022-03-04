from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core import views
from core.sitemaps import StaticViewSitemap, ImagePostSitemap, ImageGallerySitemap


sitemaps = {
    'static': StaticViewSitemap,
    'image': ImagePostSitemap,
    'gallery': ImageGallerySitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('gallery/', include('gallery.urls')),
    path('orders/', include('orders.urls')),
    path('panel/', include('panel.urls')),
    path('sitemap.xml', sitemap, {
        'sitemaps': sitemaps
    }, name='django.contrib.sitemaps.views.sitemap'),
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

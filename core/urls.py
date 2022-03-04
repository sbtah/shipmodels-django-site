from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from core import views
from core.sitemaps import StaticViewSitemap, ImagePostSitemap, ImageGallerySitemap


sitemaps = {
    'static': StaticViewSitemap,
    'image': ImagePostSitemap,
    'gallery': ImageGallerySitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel/', include('panel.urls')),
    path('sitemap.xml', sitemap, {
        'sitemaps': sitemaps
    }, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += i18n_patterns(
    path('', views.home_view, name='home'),
    path(_('o-nas/'), views.about_view, name='about'),
    path('cookies/', views.cookies_view, name='cookies'),
    path(_('polityka-prywatnosci/'),
         views.privacy_policy_view, name='privacy-policy'),
    path(_('galeria/'), include('gallery.urls')),
    path(_('zamowienia/'), include('orders.urls')),
)


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
                  path('i18n/', include('django.conf.urls.i18n')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
                       name='django.contrib.sitemaps.views'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    prefix_default_language=False,

)

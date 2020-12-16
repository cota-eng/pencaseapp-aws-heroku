from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.views.generic import TemplateView

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import environ
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
ADMIN_URL = env('ADMIN_URL')

urlpatterns = [
    path(ADMIN_URL + '/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    path('markdownx/', include('markdownx.urls')),
    path("accounts/",include("accounts.urls")),
    path("", include("pencaseapp.urls")),
    path('privacy-policy/',TemplateView.as_view(template_name="privacypolicy.html"),name="privacy-policy"),
    path('consent/',TemplateView.as_view(template_name="consent.html"),name="consent"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    print(settings.DEBUG)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 
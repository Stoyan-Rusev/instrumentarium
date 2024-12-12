from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from instrumentarium import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('instrumentarium.accounts.urls')),
    path('', include('instrumentarium.ads.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

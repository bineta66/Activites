from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

def redirect_home(request):
    if request.user.is_authenticated:
        return RedirectView.as_view(url='/activities/dashboard/', permanent=False)(request)
    return RedirectView.as_view(url='/activities/login/', permanent=False)(request)

urlpatterns = [
    path('', redirect_home),
    path('admin/', admin.site.urls),
    path('activities/', include('activities.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

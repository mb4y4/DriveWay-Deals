from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('socialaccounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'contacts.views.error_404'
handler500 = 'contacts.views.error_500'
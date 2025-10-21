
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static helper
from tours import views as tours_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tours_views.home, name='home'),
    path('tours/', include('tours.urls')),
    path('users/', include('users.urls')),
    # path('tours/', include('tours.urls')), # We'll add this later
    # path('users/', include('users.urls')), # We'll add this later
    # Add your app URLs here as you create them
]

# ONLY add these lines for development media serving
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # You might also want to serve static files this way in debug mode for simplicity, though collectstatic is for production
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
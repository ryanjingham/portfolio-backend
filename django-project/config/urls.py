from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
  path('api/', include('portfolio.urls')),
  path('admin/', admin.site.urls),
]
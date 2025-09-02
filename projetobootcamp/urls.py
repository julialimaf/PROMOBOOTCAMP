from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  
    path('api/cupom/', include('cupom_fiscal.urls')),  
    path('api/info/', include('info.urls')),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



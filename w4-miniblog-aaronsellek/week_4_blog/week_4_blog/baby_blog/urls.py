from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('week_4_blog/', include('week_4_blog.urls')),
    path('', RedirectView.as_view(url='/week_4_blog/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
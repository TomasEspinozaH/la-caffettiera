from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
	#paths del core
	path('', include('core.urls')),
	#paths del services
	path('services/', include('services.urls')),
	#paths del services
	path('blog/', include('blog.urls')),
	#paths del pages
	path('page/', include('pages.urls')),
	#paths del admin
	path('admin/', admin.site.urls),
]

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('', include('modules.web.urls')),
    path('admin/', admin.site.urls),
]

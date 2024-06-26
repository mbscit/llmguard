from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/analyzer/', include('apps.analyzer.rest.urls')),
    path('api/dispatcher/', include('apps.dispatcher.rest.urls')),
    path('api/results/', include('apps.results.rest.urls')),
    path('api/vulnerabilities/', include('apps.vulnerabilities.rest.urls')),
    path('api/auth/', include('apps.auth.urls')),

]

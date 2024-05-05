from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('mainApp.urls')),
    path('webexample/', include ('webexample.urls')),
    path('news/', include ('news.urls')),
]

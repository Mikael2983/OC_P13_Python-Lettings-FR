from django.contrib import admin
from django.urls import path, include

from . import views


handler404 = "oc_lettings_site.views.custom_error_404"
handler500 = "oc_lettings_site.views.custom_error_500"

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]

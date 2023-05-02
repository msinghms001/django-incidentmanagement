
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiv1/',include('apiv1.urls')),
    path('core/',include('core.urls')),
]

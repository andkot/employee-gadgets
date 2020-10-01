from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # rest api
    path('api/employee/', include('employee.api.urls')),

    # inner api
]

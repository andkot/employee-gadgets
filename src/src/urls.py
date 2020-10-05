from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # rest api
    # path('api/employee/', include('employee.api.urls')),
    # path('api/my_test/', include('my_test.api.urls')),
    # path('api/v1/auth/', include('rest_framework.urls')),
    # path('api/v1/students/', include('students.api.urls')),
    # path('api/v1/n_s/', include('nested_serializers.api.urls')),

    path('api/v1/staff/', include('staff.api.urls')),

    # inner api
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
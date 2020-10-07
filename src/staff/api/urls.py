from django.urls import path, include
from .views import (EmployeeView,
                    DeviceView, )
from rest_framework import routers

router = routers.SimpleRouter()
router.register('employees', EmployeeView)
router.register('devices', DeviceView)

urlpatterns = [
    path('', include(router.urls)),
]

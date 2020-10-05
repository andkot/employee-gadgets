from django.urls import path, include
from .views import (EmployeeListView,
                    EmployeeDetailsView,
                    EmployeeCreateView,
                    DeviceListView,
                    DeviceDetailsView,
                    DeviceCreateView,
                    EmployeeView,
                    DeviceView, )
from rest_framework import routers

router = routers.SimpleRouter()
router.register('employees', EmployeeView)
router.register('devices', DeviceView)

urlpatterns = [
    # path('employees/', EmployeeListView.as_view()),
    # path('employee/<pk>/details/', EmployeeDetailsView.as_view(), ),
    # path('employee/create/', EmployeeCreateView.as_view()),
    # path('devices/', DeviceListView.as_view()),
    # path('device/<pk>/details', DeviceDetailsView.as_view()),
    # path('device/create', DeviceCreateView.as_view()),

    path('', include(router.urls)),
    # path('employee/list/', EmployeeListView.as_view()),
    # path('employee/details/<pk>/', EmployeeDetailsView.as_view()),
]

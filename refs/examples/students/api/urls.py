from django.urls import path
from .views import StudentListView, StudentDetailsView

ap_name = 'employee'
urlpatterns = [
    path('list/', StudentListView.as_view()),
    path('details/<pk>/', StudentDetailsView.as_view()),
]

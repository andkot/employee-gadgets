from django.urls import path
from .views import view_1, model_1_list, model_1_details, login

urlpatterns = [
    path('view_1/', view_1),
    path('model_1_list/', model_1_list),
    path('model_1_details/<pk>', model_1_details),
    path('model_1/login/', login)
]

from django.urls import path
from .views import *

urlpatterns = [
    path('author/list/', AuthorListView.as_view()),
    path('author/details/<pk>/', AuthorDetailsView.as_view()),
    path('book/list/', BookListView.as_view()),
    path('book/details/<pk>/', BookDetailsView.as_view()),
]

from django.urls import path
from .views import LibraryDetailView

from . import views

app_name = 'relationship_app'
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from .views import LibraryDetailView
from .views import list_books, add_book, edit_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

from . import views

app_name = 'relationship_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_user, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
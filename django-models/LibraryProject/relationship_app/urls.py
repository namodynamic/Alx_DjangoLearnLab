from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .admin_view import admin_view
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard

from . import views

app_name = 'relationship_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_user, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]
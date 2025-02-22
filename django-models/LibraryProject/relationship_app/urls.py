from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin, librarian, member

from . import views

app_name = 'relationship_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_user, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin, name='admin'),
    path('librarian/', librarian, name='librarian'),
    path('member/', member, name='member'),
]
from django.urls import path

from . import views

app_name = 'bookshelf'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='list_books'),

    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
]
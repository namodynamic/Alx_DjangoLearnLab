from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access this view 
        
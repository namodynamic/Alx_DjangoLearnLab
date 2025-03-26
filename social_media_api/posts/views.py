from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.permissions import BasePermission
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the post
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
    


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        # Get the post ID from the request data and check if it exists
        post_id = self.request.data.get('post')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post does not exist")
        # Save comment with current user as author and associated post
        serializer.save(author=self.request.user, post=post)
    
    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('post')
        if post_id:
            queryset = queryset.filter(post_id=post_id)
        return queryset
    
    
class PostPagination(PageNumberPagination):
    page_size = 10
    
class FeedView(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination
    
    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
               
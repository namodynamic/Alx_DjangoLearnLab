from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import logout


def home(request):
    return render(request, template_name="blog/base.html")


def logout_view(request):
    logout(request)
    return render(request, 'blog/logout.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created, {username}! You are now able to log in')
            return redirect('blog:login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('blog:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'u_form': u_form})


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:posts')
    
    def form_valid(self, form):
        # Automatically set the author of the post to the logged-in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:posts')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return  self.request.user == post.author


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url =  reverse_lazy('blog:posts')
    items_to_delete = []
    
    def test_func(self):
        post = self.get_object()
        return  self.request.user == post.author    
    
             
        
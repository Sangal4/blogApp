from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.paginator import Paginator
from django.views.generic import (
    DetailView, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import post
context={
    'posts':post.objects.all(),
}
class post_create(LoginRequiredMixin,CreateView):
    model=post
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class post_detail(DetailView):
    model=post
class home_view(ListView):
    model=post
    template_name='polls/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']
    paginate_by = 3
class UserPostListView(ListView):
    model = post
    template_name = 'polls/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(request,'polls/about.html')
class postUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False
class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if post.author==self.request.user:
            return True
        return False

from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View
from .models import Category
from .models import Post, Comment


# class HomeView(View):
#     """Home page"""
#
#     def get(self, request):
#         category_list = Category.objects.all()
#         return render(request, "blog/home.html", {'categories': category_list})
#
#     def post(self, request):
#         pass


class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published = True)
        return render(request, "blog/post_list.html", {'categories': category_list, 'post_list': post_list})

    def post(self, request):
        pass

class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post  = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post)
        return render(request, post.template, {'categories': category_list, 'post': post,'comments':comments})

class CategoryView(View):
    """views category of staty"""
    def get(self,request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request,'blog/post_list.html', {'category': category})


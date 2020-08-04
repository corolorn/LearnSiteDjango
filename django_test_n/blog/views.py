from django.shortcuts import render
from django.views.generic.base import View
from .models import Category

class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        return render(request, "blog/home.html", {'categories': category_list})

    def post(self, request):
        pass
class CategoryView(View):
    """views category of staty"""
    def get(self,request, slug):
        category = Category.objects.get(slug=slug)
        return render(request,'blog/post_list.html', {'category': category})
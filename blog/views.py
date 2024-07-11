from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from random import randint
from django.views import View
from django.views.generic import CreateView
from .forms import AddNewBlogForm
from .models import Blog
from django.urls import reverse


class HomePageView(View):
    def get(self, request):
        form = AddNewBlogForm()
        blogs = Blog.objects.all()
        return render(request, 'blog/home_page.html', context={'form': form, 'blogs': blogs})

    def post(self, request):
        form = AddNewBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_page'))
        return render(request, 'blog/home_page.html', context={'form': form})

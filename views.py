from blog.models import Post, Category
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def index(request):
    return render(request, 'blog/index.html', {
        'categories': Category.objects.all().order_by('title'),
        'posts': Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')[:5]
    })


def view_post(request, slug):
    return render(request, 'blog/post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category, date_published__lte=timezone.now())
                             .order_by('-date_published')[:5]
    })


from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post, Category
from django.db.models import Q

current_time = timezone.now()


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        Q(is_published=True)
        & Q(category__is_published=True)
        & Q(pub_date__lte=current_time)
    ).order_by('-pub_date')[:5]

    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(Post,
                             pub_date__lte=current_time,
                             is_published=True,
                             category__is_published=True,
                             id=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, is_published=True,
                                 slug=category_slug)
    post_list = category.posts.filter(
        Q(is_published=True)
        & Q(pub_date__lte=current_time)
    )
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)

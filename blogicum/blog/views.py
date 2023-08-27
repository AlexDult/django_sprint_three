from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.http import Http404

from datetime import datetime


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        pub_date__lte=datetime.now().date(),
        is_published=True,
        category__is_published=True).order_by('-pub_date')[:5] #два нижних подчеркивания означает "перейди по внешнему
    # ключу к полю is_published
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    # found_category = None
    # all_categories_from_my_db = Category.objects.all() # для того чтобы обратиться к  slug

    # модели Category, нужна конструкция 'objects.all()'
    # Category.objects - manager (django calls this attribute)
    # manager = Category.objects
    # get one model - manager.get()
    # get all models - manager.all()
    # get some models - manager.filter()

    # for category in all_categories_from_my_db:
    #     if category.slug == category_slug:
    #         found_category = category
    #         break

    # for post_slug in Category.slug:
    #     if Category.slug == post_slug:
    #         found_post = post_slug
    #         break

    # found_post = get_object_or_404(Post, slug=post_slug)

    try:
        post = Post.objects.get(id=post_id, pub_date__lte=datetime.now().date(),
                                is_published=True,
                                category__is_published=True)
    except Post.DoesNotExist:
        raise Http404()

    template_name = 'blog/detail.html'
    # post_list_1 = Post.objects.values('title', 'location',
    #                                   'location.name', 'pub_date', 'text').filter(is_published=True)
    # context = {
    #     'post_list_1': post_list_1,
    # }
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):

    # post_list = Category.objects.values('title', 'description').filter(slug=category_slug,
    #                                                                     is_published=True,
    #                                                                     created_at__lte=datetime.now().date()),
    try:
        category = Category.objects.get(slug=category_slug, is_published=True)
    except Category.DoesNotExist:
        raise Http404()
    # query category from db by category_slug

    # if category does not exist
    #    raise 404

    # query category's posts from db
    posts = Post.objects.filter(category=category, is_published=True, pub_date__lte=datetime.now().date())
    # pass them to context

    #try:
    #post_list = Post.objects.filter(   # метод не filter не генерирует исключения Post.DoesNotExist
    #    pub_date__lte=datetime.now().date(),
    #    is_published=True,
    #    category__is_published=True,
    #    category__slug=category_slug)
    #except Post.DoesNotExist:

    #if not post_list:
    #    raise Http404()

    template_name = 'blog/category.html'
    context = {
        'category': category,
        'post_list': posts,
    }
    return render(request, template_name, context)


def category_link(request):
    template_name = 'blog/category_link.html'
    post_list_3 = Post.objects.values('category.title', 'category.slug')
    context = {
        'post_list_3': post_list_3,
    }
    return render(request, template_name, context)


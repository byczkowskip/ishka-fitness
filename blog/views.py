from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class PostsListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet:
        queryset =  Post.objects.filter(is_active=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_object(self, queryset: QuerySet|None = None) -> Post:
        category_slug = self.kwargs.get('category_slug')
        post_slug = self.kwargs.get('post_slug')
        return get_object_or_404(Post,
                                 slug=post_slug,
                                 category__slug=category_slug,
                                 is_active=True)

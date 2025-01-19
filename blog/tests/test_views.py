import pytest
from django.urls import reverse
from django.test import RequestFactory
from blog.models import Post, Category
from blog.views import PostsListView, PostDetailView

@pytest.fixture
def category():
    return Category.objects.create(name='Test Category', slug='test-category')

@pytest.fixture
def post(category):
    return Post.objects.create(
        title='Test Post',
        slug='test-post',
        description='Test description',
        category=category,
        is_active=True
    )

@pytest.fixture
def request_factory():
    return RequestFactory()

@pytest.mark.django_db
def test_posts_list_view_with_active_posts(request_factory, post):
    request = request_factory.get(reverse('blog:blog'))
    view = PostsListView.as_view()
    response = view(request)
    assert response.status_code == 200
    assert 'posts' in response.context_data
    assert post in response.context_data['posts']

@pytest.mark.django_db
def test_posts_list_view_with_category(request_factory, post, category):
    request = request_factory.get(reverse('blog:category', kwargs={'category_slug': category.slug}))
    view = PostsListView.as_view()
    response = view(request, category_slug=category.slug)
    assert response.status_code == 200
    assert 'posts' in response.context_data
    assert post in response.context_data['posts']
    assert response.context_data['posts'][0].category == category

@pytest.mark.django_db
def test_post_detail_view(request_factory, post):
    request = request_factory.get(reverse('blog:category_post', kwargs={
        'category_slug': post.category.slug,
        'post_slug': post.slug
    }))
    view = PostDetailView.as_view()
    response = view(request, category_slug=post.category.slug, post_slug=post.slug)
    assert response.status_code == 200
    assert 'post' in response.context_data
    assert response.context_data['post'] == post

import pytest
from django.urls import reverse, resolve
from blog.views import PostsListView, PostDetailView

@pytest.mark.django_db
def test_blog_url():
    url = reverse('blog:blog')
    assert resolve(url).func.view_class == PostsListView

@pytest.mark.django_db
def test_category_url():
    url = reverse('blog:category', kwargs={'category_slug': 'test-category'})
    assert resolve(url).func.view_class == PostsListView

@pytest.mark.django_db
def test_category_post_url():
    url = reverse('blog:category_post', kwargs={'category_slug': 'test-category', 'post_slug': 'test-post'})
    assert resolve(url).func.view_class == PostDetailView

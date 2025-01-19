import pytest
from blog.models import Category, Post
from django.urls import reverse_lazy

@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(
        name="Test Category",
        slug="test-category",
        is_active=True
    )
    assert category.name == "Test Category"
    assert category.slug == "test-category"
    assert category.is_active is True
    assert str(category) == "Test Category"
    assert category.get_absolute_url() == reverse_lazy('blog:category', kwargs={'category_slug': 'test-category'})

@pytest.mark.django_db
def test_post_model():
    category = Category.objects.create(
        name="Test Category",
        slug="test-category",
        is_active=True
    )
    post = Post.objects.create(
        category=category,
        title="Test Post",
        slug="test-post",
        description="This is a test post.",
        is_active=True
    )
    assert post.title == "Test Post"
    assert post.slug == "test-post"
    assert post.description == "This is a test post."
    assert post.is_active is True
    assert post.category == category
    assert str(post) == "Test Post"
    assert post.get_absolute_url() == reverse_lazy('blog:category_post',
                                                   kwargs={'category_slug': 'test-category', 'post_slug': 'test-post'})
    assert post.intro == "This is a test post."

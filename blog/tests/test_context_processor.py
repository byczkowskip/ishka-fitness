import pytest
from django.http import HttpRequest
from blog.models import Category
from blog.context_processor import blog_categories

@pytest.mark.django_db
def test_blog_categories_context_processor():
    # Create some test categories
    Category.objects.create(name='Category 1', slug='category-1', is_active=True)
    Category.objects.create(name='Category 2', slug='category-2', is_active=False)
    Category.objects.create(name='Category 3', slug='category-3', is_active=True)

    # Create a mock request
    request = HttpRequest()

    # Call the context processor
    context = blog_categories(request)

    # Check the context data
    assert 'blog_categories' in context
    categories = context['blog_categories']
    assert categories.count() == 2  # Only the active categories should be returned
    assert categories.filter(name='Category 1').exists()
    assert categories.filter(name='Category 3').exists()
    assert not categories.filter(name='Category 2').exists()

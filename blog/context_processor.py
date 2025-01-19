from django.db.models import QuerySet
from django.http import HttpRequest

from blog.models import Category


def blog_categories(request: HttpRequest) -> dict[str, QuerySet]:
    categories = Category.objects.filter(is_active=True)
    return {'blog_categories': categories}

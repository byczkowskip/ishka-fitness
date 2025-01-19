from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=250,
                            blank=False,
                            null=False)
    slug = models.SlugField(max_length=250)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def get_absolute_url(self) -> str:
        return reverse_lazy('blog:category',
                            kwargs={
                                'category_slug': self.slug
                            })

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='posts',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=250,
                             blank=False,
                             null=False)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['title']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['title']),
            models.Index(fields=['category', 'is_active']),
        ]

    @property
    def intro(self) -> str:
        if len(self.description) > 400:
            return self.description[:400] + '...'
        return self.description

    def get_absolute_url(self) -> str:
        return reverse_lazy('blog:category_post',
                            kwargs={
                                'category_slug': self.category.slug,
                                'post_slug': self.slug
                            })

    def __str__(self) -> str:
        return self.title

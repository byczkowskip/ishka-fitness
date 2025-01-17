from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250,
                            blank=False,
                            null=False)
    slug = models.SlugField(max_length=250)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

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
    description = models.TextField(max_length=400)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['title']),
            models.Index(fields=['category', 'is_active']),
        ]

    def __str__(self) -> str:
        return self.title



from django.contrib.auth.models import User
from django.db import models


class Technology(models.Model):
    """Model definition for Technology."""

    name = models.CharField(max_length=100)
    class Meta:
        """Meta definition for Technology."""

        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        """Unicode representation of Technology."""
        return self.name

class Portfolio(models.Model):
    """Model definition for Portfolio."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    technology = models.ManyToManyField(Technology)
    cover = models.ImageField(
        upload_to='portfolio/covers/%Y/%m/%d/',
        default='portfolio/covers/default.jpg'
    )
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        """Meta definition for Portfolio."""

        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        """Unicode representation of Portfolio."""

        return self.title

class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""

        return self.name

from django.db import models

# Create your models here.
class Category(models.Model):
    """model of category"""
    name = models.CharField('Ghost', max_length=50)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
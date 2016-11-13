from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Категории')
    view = models.IntegerField(default=0, verbose_name='Просмотры')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    slug = models.SlugField()

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категирия'
        verbose_name_plural = 'Категории'

class Page(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категории')
    title = models.CharField(max_length=128, verbose_name='стр')
    url = models.URLField(verbose_name='URL')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

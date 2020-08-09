from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils import timezone


class Category(MPTTModel):
    """model of category"""
    name = models.CharField('Ghost', max_length=50)
    slug = models.SlugField("url", max_length=100)
    description = models.TextField('Описание', max_length=1000, default="", blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField('Шаблон', max_length=500, default="blog/post_list.html")
    publihed = models.BooleanField('Отображать', default=True)
    paginated = models.PositiveIntegerField('Количество новостей на странице', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('fix', max_length=50)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    """Модель постов"""
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField('title', max_length=100)
    mini_text = models.TextField('m_text', max_length=250)
    text = models.TextField('f_text', max_length=5000000)
    created_date = models.DateTimeField('created_date', auto_now_add=True)
    slug = models.SlugField("url", max_length=100)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True)
    subtitle = models.CharField("Под заголовок", max_length=500, blank=True, null=True)
    edit_date = models.DateTimeField(
        'Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
    template = models.CharField('Шаблон',max_length=500, default='blot/post_detail.html')

    published = models.BooleanField('Опубликовать?', default=True)
    viewed = models.PositiveIntegerField('Просмотрено',default=0)
    status = models.BooleanField('для зарегестрированных',default=False)
    sort = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_urls(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    "Модель комментариев постов"
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    text = models.TextField('f_text', max_length=400)
    created_date = models.DateTimeField('created_date')
    moderation = models.BooleanField('moderation')
    post = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)

    # def __str__(self):
    #     return '%s (%s)' % (self.created_date,self.post.title)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

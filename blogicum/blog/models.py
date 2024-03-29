
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
# Create your models here.


class Category (models.Model):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True, help_text='Идентификатор страницы для URL; '
                                                                    'разрешены символы латиницы, '
                                                                    'цифры, дефис и подчёркивание.')
    is_published = models.BooleanField('Опубликовано', default=True,  help_text='Снимите галочку, '
                                                                                'чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location (models.Model):
    name = models.CharField('Название места', max_length=256)
    is_published = models.BooleanField('Опубликовано', default=True,  help_text='Снимите галочку, '
                                                                                'чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post (models.Model):
    title = models.CharField('Название', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации',  help_text='Если установить дату и время в будущем — '
                                                                          'можно делать отложенные публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    is_published = models.BooleanField('Опубликовано', default=True,  help_text='Снимите галочку, '
                                                                                'чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title

# после создания моделей, их нужно создать в БД, для этого предварительно : 1) python manage.py makemigrations
# 2) python manage.py sqlmigrate blog 0001
# 3) python manage.py migrate





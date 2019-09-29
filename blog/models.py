from django.db import models
from django.urls import reverse
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Slider(models.Model):
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    sort = models.IntegerField(default=0, verbose_name='Номер для сортировки')
    title = models.CharField(max_length=255, null=True, verbose_name='Название слайда')
    image = models.ImageField(upload_to='media/', null=True, verbose_name='Изображение слайда')
    description = models.TextField(null=True, verbose_name='Описание')
    link_text = models.CharField(max_length=50, null=True, verbose_name='Текст ссылки')
    link = models.URLField(null=True, max_length=200)

    def __str__(self):
        return '{}'.format(self.title)


class AbstractPage(models.Model):
    slug = models.SlugField(max_length=100, blank=True, null=True, db_index=True, unique=True, verbose_name='uri')
    public = models.BooleanField(null=True, default=False, verbose_name='Опубликовать')
    date_pub = models.DateTimeField(auto_now_add=False, blank=True, verbose_name='Создан')
    image = models.ImageField(blank=True, upload_to='media/', null=True, verbose_name='Изображение для превью')
    short_description = RichTextUploadingField(null=True, verbose_name='Короткое описание статьи')
    # detail_image = models.ImageField(upload_to='media/', null=True, verbose_name='Детальное изображение')
    description =  RichTextUploadingField(null=True, verbose_name='Полное описание статьи')

    class Meta:
        abstract = True
        ordering = ['date_pub']


class LonggridTag(models.Model):
    name = models.CharField(null=True, unique=True, max_length=50, verbose_name='Тэг лонггрида')
    slug = models.SlugField(max_length=50, null=True,
                            db_index=True, unique=True,
                            verbose_name='uri', help_text='Поле задает уникалный адрес объекта в разделе сайта')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:longgrid_tag_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class Longgrid(AbstractPage):
    title = models.CharField(max_length=150, null=True, verbose_name='Название Лонггрида')
    tags = models.ManyToManyField(LonggridTag, blank=True, verbose_name="Теги статьи Longgrid", related_name="Longgrids")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Лонггрид"
        verbose_name_plural = "Лонггриды"


class NBATag(models.Model):
    name = models.CharField(null=True, unique=True, max_length=50, verbose_name='Тэг NBA')
    slug = models.SlugField(max_length=50, null=True,
                            db_index=True, unique=True,
                            verbose_name='uri', help_text='Поле задает уникалный адрес объекта в разделе сайта')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:nba_tag_url', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class NBA(AbstractPage):
    title = models.CharField(max_length=150, null=True, verbose_name='Название статьи NBA')
    tags = models.ManyToManyField(NBATag, blank=True, verbose_name="Теги статьи NBA", related_name="NBA")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NBA"
        verbose_name_plural = "NBAs"
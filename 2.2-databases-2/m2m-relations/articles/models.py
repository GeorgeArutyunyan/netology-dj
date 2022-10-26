from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tag = models.ManyToManyField(Tag, through='Scope', related_name='articles', verbose_name='Тема статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scope')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

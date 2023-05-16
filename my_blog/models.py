from django.db import models

# Create your models here.
class Post(models.Model):
    """Основная модель"""
    title = models.CharField('Заголовок',max_length=100)
    descriptions = models.TextField('Текст поста')
    author = models.CharField('Автор',max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображения',upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title}{self.author}'
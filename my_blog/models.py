from django.db import models


# Create your models here.
class Post(models.Model):
    """Основная модель"""
    title = models.CharField('Заголовок', max_length=100)
    descriptions = models.TextField('Текст поста')
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации', auto_now=True)
    img = models.ImageField('Изображения', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title}{self.author}'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name}{self.post}'


class Likes(models.Model):
    ip = models.CharField('ip адрес', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

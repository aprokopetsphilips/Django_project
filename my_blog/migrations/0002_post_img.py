# Generated by Django 4.2.1 on 2023-05-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='some.image', upload_to='image/%Y', verbose_name='Изображения'),
            preserve_default=False,
        ),
    ]

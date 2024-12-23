# Generated by Django 5.1.3 on 2024-12-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/', verbose_name='Загрузите фото Книги')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название книги')),
                ('description', models.TextField(blank=True, verbose_name='Укажите описание')),
                ('price', models.FloatField(default=25, verbose_name='Задайте цену книги')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('Хоррор', 'Хоррор'), ('Комедия', 'Комедия'), ('Детектив', 'Детектив')], default='Детектив', max_length=100)),
                ('author_gmail', models.EmailField(max_length=254, verbose_name='Укажите эл.почту автора')),
                ('author', models.CharField(default='Туратбеков алибек', max_length=100, verbose_name='Укажите автора')),
                ('audio_book', models.URLField(verbose_name='Укажите ссылку аудио книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]

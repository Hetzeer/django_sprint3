# Generated by Django 3.2.16 on 2024-11-18 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(auto_created=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateField(auto_created=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_created=True, verbose_name='Добавлено'),
        ),
    ]

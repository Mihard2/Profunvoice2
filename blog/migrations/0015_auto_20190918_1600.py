# Generated by Django 2.1.1 on 2019-09-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190918_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longgrid',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='longgrids', to='blog.LonggridTag', verbose_name='Теги статьи Longgrid'),
        ),
    ]

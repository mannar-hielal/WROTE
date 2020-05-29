# Generated by Django 3.0.6 on 2020-05-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200529_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_de',
            field=models.TextField(null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=models.TextField(null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='post',
            name='body_fr',
            field=models.TextField(null=True, verbose_name='Body'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_de',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_fr',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
    ]

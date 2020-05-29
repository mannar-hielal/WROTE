# Generated by Django 3.0.6 on 2020-05-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200529_0741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_de',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_fr',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_de',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_fr',
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Title'),
        ),
    ]

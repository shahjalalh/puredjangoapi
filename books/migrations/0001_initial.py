# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-26 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Book Name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(help_text='Genre of the book', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(blank=True, help_text='Book Genre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.BookGenre'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserProfile'),
        ),
    ]

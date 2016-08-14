# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 12:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_style', django_mysql.models.EnumField(choices=[('informational', 'informational'), ('opinion', 'opinion')])),
                ('article_type', django_mysql.models.EnumField(choices=[('feature', 'feature'), ('regular', 'regular')])),
                ('co_author', models.CharField(blank=True, max_length=64)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cycle_article', models.BooleanField(default=False)),
                ('description', django_mysql.models.SizedTextField(blank=True, size_class=2)),
                ('feature_image', models.ImageField(blank=True, upload_to='')),
                ('header_image', models.ImageField(blank=True, upload_to='')),
                ('photo_credit', models.CharField(blank=True, max_length=255)),
                ('published_date', models.DateTimeField(blank=True)),
                ('search_terms', django_mysql.models.ListCharField(models.CharField(blank=True, max_length=36), blank=True, max_length=740, size=20)),
                ('slug', models.CharField(blank=True, editable=False, max_length=255)),
                ('status', django_mysql.models.EnumField(choices=[('published', 'published'), ('queued', 'queued'), ('ready', 'ready'), ('draft', 'draft')])),
                ('tags', django_mysql.models.ListCharField(models.CharField(blank=True, max_length=36), blank=True, max_length=740, size=20)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'db_table': 'dashboard_article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('status', django_mysql.models.EnumField(choices=[('pending', 'pending'), ('reviewed', 'reviewed')], default='pending')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'dashboard_comment',
            },
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('description', django_mysql.models.SizedTextField(blank=True, size_class=2)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('is_current', models.BooleanField(default=False)),
                ('articles', models.ManyToManyField(blank=True, related_name='cycles', related_query_name='rotation', to='blog.Article')),
            ],
            options={
                'db_table': 'dashboard_cycle',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('role', models.CharField(choices=[('F', 'Founder'), ('M', 'Member'), ('C', 'Contributor'), ('W', 'Staff Writer')], default='M', editable=False, max_length=1)),
                ('bio', django_mysql.models.SizedTextField(blank=True, size_class=2)),
                ('linkedin', models.CharField(blank=True, max_length=128)),
                ('pinterest', models.CharField(blank=True, max_length=128)),
                ('facebook', models.CharField(blank=True, max_length=128)),
                ('instagram', models.CharField(blank=True, max_length=128)),
                ('twitter', models.CharField(blank=True, max_length=128)),
                ('tumblr', models.CharField(blank=True, max_length=128)),
                ('website', models.CharField(blank=True, max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'dashboard_member',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_parent', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('description', django_mysql.models.SizedTextField(blank=True, size_class=2)),
                ('subcategory', models.ManyToManyField(blank=True, related_name='_topic_subcategory_+', to='blog.Topic')),
            ],
            options={
                'db_table': 'dashboard_topic',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='topics', related_query_name='category', to='blog.Topic'),
        ),
        migrations.AddField(
            model_name='article',
            name='cycle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cycle'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-24 13:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('content', ckeditor.fields.RichTextField()),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('post_banner', models.ImageField(upload_to='blogpost/')),
            ],
        ),
    ]
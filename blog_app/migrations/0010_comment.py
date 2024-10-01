# Generated by Django 5.0.4 on 2024-05-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_commentpost_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField(default=0)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
    ]
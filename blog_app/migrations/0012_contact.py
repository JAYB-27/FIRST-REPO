# Generated by Django 5.0.4 on 2024-05-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.PositiveIntegerField()),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]

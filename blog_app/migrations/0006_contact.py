# Generated by Django 5.0.4 on 2024-04-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_authorprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.PositiveIntegerField(max_length=15)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]

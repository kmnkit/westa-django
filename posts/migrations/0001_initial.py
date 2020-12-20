# Generated by Django 3.1.4 on 2020-12-20 09:51

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=posts.models.Post.upload_path)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

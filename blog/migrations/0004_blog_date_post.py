# Generated by Django 4.2.7 on 2024-07-11 11:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date_post',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.7 on 2024-07-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_name_blog_blog_text_blog_photo_blog_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.FileField(blank=True, upload_to='blogs_content'),
        ),
    ]
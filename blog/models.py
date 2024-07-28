from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from transliterate import translit


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    photo = models.FileField(upload_to='blogs_content', blank=True, null=False)
    blog_text = models.CharField(max_length=500, blank=True, null=False)
    autor = models.CharField(max_length=50, blank=False, null=False)
    date_post = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False)

    def __str__(self):
        return f'{self.title} {self.autor} {self.date_post}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(translit(f"{self.title} {self.autor}", 'ru', reversed=True)
                                )
        super(Blog, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one_blog_info', args=[self.slug])

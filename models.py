from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    date_published = models.DateTimeField('date published', db_index=True)
    category = models.ForeignKey('blog.Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

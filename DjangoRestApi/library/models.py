from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20,
                                blank=False,
                                default='')

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['category']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Book(models.Model):
    title = models.CharField(max_length=70,
                             blank=False,
                             default='')
    author = models.CharField(max_length=70,
                              blank=False,
                              default='')
    description = models.CharField(max_length=1000,
                                   default='')
    category = models.ManyToManyField(Category)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

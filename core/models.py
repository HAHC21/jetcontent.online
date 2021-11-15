from django.db import models


class Site(models.Model):
    """
    Sites
    """
    name = models.CharField(max_length=150, verbose_name="Name", unique=True)
    prefix = models.CharField(max_length=4, verbose_name="Prefix", unique=True, blank=True, null=True)
    logo = models.ImageField(upload_to='sites/%Y/%m/%d', null=True, blank=True)
    url = models.CharField(max_length=150, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
        db_table = "core_sites"
        ordering = ['name']


class Article(models.Model):
    """
    Article
    """
    site = models.ForeignKey(Site, related_name='site', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name="Name", unique=True)
    content = models.TextField()
    url = models.CharField(max_length=150, verbose_name="URL")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        db_table = "core_articles"
        ordering = ['title']

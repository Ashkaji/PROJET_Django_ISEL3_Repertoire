from django.db import models

# Create your models here.
from django.utils.text import slugify
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    tel = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.date:
            self.date = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Contact"

    def __str__(self):
        return self.name

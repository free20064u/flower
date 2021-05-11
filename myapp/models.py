from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()




class Category(models.Model):
    title = models.CharField(max_length=222, default='')

    def __str__(self):
        return f"Category: { self.title }"

class Flower(models.Model):
    title   = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    slug = models.SlugField(blank=True, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(default='', blank=True, upload_to="images")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 100)], format='jpeg', options={'quality': 60})


    def __str__(self):
        return f"Title: { self.title }"


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Flower, self).save()

    def get_absolute_url(self):
        return reverse("detail", args={self.slug})
    
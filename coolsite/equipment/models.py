from django.db import models
from django.urls import reverse
class Equipment(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_id': self.pk})
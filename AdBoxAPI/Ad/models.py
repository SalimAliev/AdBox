from django.db import models

# Create your models here.


class AdPhoto(models.Model):
    objects = models.Manager()
    advertisement = models.ForeignKey('Ad', on_delete=models.CASCADE, related_name='photos')
    image_path = models.CharField(max_length=200)


class Ad(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    data_create = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField()
    current_price = models.IntegerField()
    real_price = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
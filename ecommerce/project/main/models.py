from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/cat_imgs/")

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/brand_imgs/")

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# product model


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/prod_imgs/")
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

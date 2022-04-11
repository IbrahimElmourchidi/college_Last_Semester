from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    c_name      = models.CharField(max_length=50, null=False)
    added_by    = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.c_name



class Product(models.Model):
    p_name          = models.CharField(max_length=50, null=False, unique=False)
    p_description   = models.TextField(null=True)
    p_price         = models.FloatField(null=False)
    Category        = models.ForeignKey(Category, on_delete= models.CASCADE)


    def __str__(self):
        return self.p_name
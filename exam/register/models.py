from unicodedata import category
from urllib.parse import MAX_CACHE_SIZE
from django.db import models


class Category(models.Model):
    name_cat = models.CharField(max_length=30)
    first_num = models.IntegerField()
    balance_gr = models.IntegerField()

    def __str__(self):
        return self.name_cat


class Product(models.Model):
    name_prod = models.CharField(max_length=30)
    category_prod = models.ForeignKey(Category, on_delete=models.CASCADE)
    inv_number = models.IntegerField(unique=True)
    start_price = models.IntegerField()
    rem_price = models.IntegerField()

    def __str__(self):
        return self.name_prod


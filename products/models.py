from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Sumkalar(models.Model):
    narhi=models.DecimalField(max_digits=12,decimal_places=2)
    rangi=models.CharField(max_length=120)
    hajmi=models.CharField(max_length=120)
    categorys=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.rangi

# Create your models here.

from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    favorite_categories = models.ManyToManyField('Category', related_name='buyers', blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

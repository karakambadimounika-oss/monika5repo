from django.db import models

# Create your models here.

class FoodItem(models.Model):

    food_name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(max_length=100)

    image = models.ImageField(upload_to='food_images/')

    def __str__(self):
        return self.food_name


class Order(models.Model):

    customer_name = models.CharField(max_length=100)

    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    order_date = models.DateTimeField(auto_now_add=True)
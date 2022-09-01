from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class cuisine(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category

class Food(models.Model):
    category = models.ForeignKey(cuisine, on_delete = models.DO_NOTHING)
    # on_delete_cascade ---> all tables will be deleted
    # do_nothing -----> keeps the data in other table

    name = models.CharField(max_length = 100)
    description = models.TextField()
    secondery_desscription = models.TextField(blank = True)
    price = models.FloatField()
    is_available = models.BooleanField(default = True)
    image = models.ImageField(upload_to = "food_images/")

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    order_details = models.CharField(max_length=500)
    total_price = models.FloatField()
    is_ready = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
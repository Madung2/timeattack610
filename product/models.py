from django.db import models
from user.models import UserModel


# Create your models here.
# from user.models import UserModel

#Create your models here.
class ProductModel(models.Model):
    class Meta:
        db_table = "products"
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='uploads/', null=True)
    description = models.CharField(max_length=200, null=True)
    cost = models.IntegerField( null=True)
    stock = models.IntegerField( null=True)

class Category(models.Model):
    class Meta:
        db_table = "category"
    def __str__(self):
        return self.category
    category = models.CharField(max_length=50, default='')


class ProductOrder(models.Model):
    class Meta:
        db_table = "product_order"
    def __str__(self):
        return self.product
    orderid =models.IntegerField( null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    number = models.IntegerField( null=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True)

class UserOrder(models.Model):
    class Meta:
        db_table = "user_order"
    def __str__(self):
        return self.user

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    cost = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=False)
    discount = 1
    valid = models.BooleanField(default=True)



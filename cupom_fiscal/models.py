from django.db import models
from users.models import CustomUser

class Product(models.Model):
    id_item = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name


class FiscalCoupon(models.Model):
    
    cnpj = models.CharField(max_length=18, default='00.000.000/0000-00')
    user_fk = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cupons')
    image = models.ImageField(upload_to='midias/', default='default.jpg')
    products = models.ManyToManyField(Product, through='Pivo', related_name='coupons')
    date_register = models.DateTimeField(auto_now_add=True)
  


    def __str__(self):
        return f"{self.user_fk.username} - Cupom {self.id}"


class Pivo(models.Model):
    coupon = models.ForeignKey(FiscalCoupon, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    
    def __str__(self):
        return f"{self.product.product_name} x {self.quantity} (Cupom {self.coupon.id})"

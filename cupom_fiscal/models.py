from django.db import models
from django.conf import settings
from django.utils import timezone   
from django.db import models
from users.models import CustomUser  

class FiscalCoupon(models.Model):
    id = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=18, default='00.000.000/0000-00')
    user_fk = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cupons')
    image = models.ImageField(upload_to='midias/', default='default.jpg')
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.user_fk.username}"
    











class ItemProduct(models.Model):
    id_item = models.AutoField(primary_key= True)
    
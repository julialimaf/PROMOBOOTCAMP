from django.db import models
from users.models import CustomUser
from cupom_fiscal.models import FiscalCoupon
from django.utils import timezone

class LuckyNumberControl(models.Model):
    batch = models.IntegerField("Batch")
    series = models.IntegerField("Series")
    max_series = models.IntegerField("Max Series")
    number = models.ForeignKey('LuckyNumber', on_delete=models.CASCADE, related_name='number_controls')

    def __str__(self):
        return f"Number: {self.number} - Batch: {self.batch} - Series: {self.series}"


class LuckyNumber(models.Model):
    number = models.IntegerField("Lucky Number", unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='lucky_numbers')
    coupon = models.ForeignKey(FiscalCoupon, on_delete=models.CASCADE, related_name='lucky_numbers')
    created_at = models.DateTimeField("Created At", default=timezone.now)


    def __str__(self):
        return f"Number: {self.number} - User: {self.user.cpf} - Coupon: {self.coupon.id}"

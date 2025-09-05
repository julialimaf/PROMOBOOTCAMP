import random
from django.db import IntegrityError, transaction
from .models import LuckyNumber, LuckyNumberControl

MAX_SERIES = 99999
MAX_TRIES = 1000  

def _get_last_batch():
    last = LuckyNumberControl.objects.order_by('-id').first()
    return last.batch if last else 0

def _next_batch(start_batch):
    next_b = (start_batch % 99) + 1
    return next_b

def generate_numbers_for_coupon(coupon, user, quantity):
    generated = []
    start_batch = _get_last_batch()

    for _ in range(int(quantity)):
        batch = _next_batch(start_batch)
        attempt = 0
        while attempt < MAX_TRIES:
            series = random.randint(0, MAX_SERIES)  
            number_int = f"{batch}{str(series).zfill(6)}"  
            try:
                with transaction.atomic():
                    number_obj = LuckyNumber.objects.create(
                        number=number_int,
                        user=user,
                        coupon=coupon
                    )
                    LuckyNumberControl.objects.create(
                        batch=batch,
                        series=series,
                        max_series=MAX_SERIES,
                        number=number_obj
                    )
                generated.append(number_obj)
                
                start_batch = batch
                break
            except IntegrityError:
                attempt += 1
                continue
        else:
            raise RuntimeError(f"Sorry, limit reached: {MAX_TRIES} attempts (batch {batch}).")
    return generated

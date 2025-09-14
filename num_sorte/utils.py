import random
from django.db import IntegrityError, transaction
<<<<<<< HEAD
from .models import LuckyNumber, LuckyNumberControl
from users.models import CustomUser 
generated = []
MAX_SERIES = 99999
MAX_TRIES = 1000  

def _get_last_batch():
    last = LuckyNumberControl.objects.order_by('-id').first()
    return last.batch if last else 0

def _next_batch(start_batch):
    next_b = (start_batch % 98) + 1
    return next_b

def generate_numbers_for_coupon(coupon, user, quantity):
    start_batch = _get_last_batch()

    for _ in range(int(quantity)):
        batch = _next_batch(start_batch)
        attempt = 0
        while attempt < MAX_TRIES:
            series = random.randint(0, MAX_SERIES)  
            number_int = f"{batch}{str(series).zfill(5)}"  
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
=======
from .models import NumeroSorte, ControleNumeroSorte

MAX_SERIE = 99999
MAX_TRIES = 1000  

def _get_last_lote():
    last = ControleNumeroSorte.objects.order_by('-id').first()
    return last.lote if last else 0

def _next_lote(start_lote):
   
    next_l = (start_lote % 9) + 1
    return next_l

def generate_numeros_para_cupom(cupom, usuario, quantidade):
    
    gerados = []
    start_lote = _get_last_lote()

    for _ in range(int(quantidade)):
        lote = _next_lote(start_lote)
        attempt = 0
        while attempt < MAX_TRIES:
            serie = random.randint(0, MAX_SERIE)  
            numero_int = lote * 100000 + serie
            try:
                with transaction.atomic():
                    numero_obj = NumeroSorte.objects.create(
                        numero=numero_int,
                        usuario=usuario,
                        cupom_fiscal=cupom
                    )
                    ControleNumeroSorte.objects.create(
                        lote=lote,
                        serie=serie,
                        max_serie=MAX_SERIE,
                        numero=numero_obj
                    )
                gerados.append(numero_obj)
                
                start_lote = lote
                break
            except IntegrityError:
                
                attempt += 1
                continue
        else:
          
            raise RuntimeError(f"Não foi possível gerar número único após {MAX_TRIES} tentativas (lote {lote}).")
    return gerados
>>>>>>> 43286f0 (pegar so o cupom e o numero)

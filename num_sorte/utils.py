import random
from django.db import IntegrityError, transaction
from .models import NumeroSorte, ControleNumeroSorte

MAX_SERIE = 99999
MAX_TRIES = 1000  

def _get_last_lote():
    last = ControleNumeroSorte.objects.order_by('-id').first()
    return last.lote if last else 0

def _next_lote(start_lote):
   
    next_l = (start_lote % 10) + 1
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
          
            raise RuntimeError(f"Foi mal, o limite chegou:  {MAX_TRIES} tentativas (lote {lote}).")
    return gerados
from num_sorte.models import ControleNumeroSorte
import random
from cupom_fiscal.models import CupomFiscal



def gerar_numeros_sorte(cupom, max_serie=99999):
    numeros = []
    lote_atual = 1

    for _ in range(cupom.quantidade):
        if lote_atual > 9:
            lote_atual = 1

        serie = random.randint(10000, max_serie)
        numero_str = f"{lote_atual}.{serie}"

        controle_numero = ControleNumeroSorte.objects.create(
            cupom=cupom,
            lote=lote_atual,
            serie=serie,
            numero=numero_str
        )
        numeros.append(controle_numero)

        lote_atual += 1

    return numeros

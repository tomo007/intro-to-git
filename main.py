from web import dohvati_5_kripto_valuta
from kripto_valuta import KriptoValuta

if __name__ == "__main__":
    kripto_valute = dohvati_5_kripto_valuta()

    for valuta in kripto_valute:
        print(valuta)

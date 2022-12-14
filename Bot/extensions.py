from config import keys
import json
import requests


class ConvertionException(Exception):
    pass


class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Нельзя перевести одинаковые валюты: {base}!')

        try:
            quote_Tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту: {quote}!')

        try:
            base_Tiker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту: {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество!{amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_Tiker}&tsyms={base_Tiker}')
        totalbase = json.loads(r.content)[keys[base]]

        return totalbase * amount

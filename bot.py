import sys
from multiprocessing import Process
import requests
from pybit import spot
import time

session = spot.HTTP(
    endpoint='https://api.bybit.com',
    api_key='2TeoahEHkSmEePu1M8',
    api_secret='PGaakmqwAmnJPrZ1loZ53rU3vmhH44noWIvN',
)

symbols_1 = ['TRX', 'DOT', 'TRX', 'NEO', 'AVAX', 'ADA', 'MIR', 'AAVE']
symbols_2 = ['SOL', 'LINK', 'KCS', 'GMT', 'ACQ', 'DASH', 'VRA', 'NEO']
symbols_3 = ['HFT', 'LTC', 'APE', 'EOS', 'MJT', 'OP', 'XLM', 'VET']


def get_prices(crypto):
    priceusdt = 0
    priceusdc = 0
    priceusd = 0
    prises = session.latest_information_for_symbol()['result']
    for prise in prises:
        if prise['symbol'] == crypto + 'USDT':
            priceusdt = prise['lastPrice']
            if priceusdc != 0 and priceusd != 0:
                break
        elif prise['symbol'] == crypto + 'USDC':
            priceusdc = prise['lastPrice']
            if priceusdt != 0 and priceusd != 0:
                break
        elif prise['symbol'] == 'USDCUSDT':
            priceusd = prise['lastPrice']
            if priceusdt != 0 and priceusdc != 0:
                break
    return [float(priceusd), float(priceusdt), float(priceusdc)]


def start(crypto_symbol):
    while True:
        try:
            for symbol in crypto_symbol:
                first, second, third = get_prices(symbol)
                percent = (first / second * third - 1) * 100
                print(symbol)
                print(second)
                print(third)
                print(percent, '%')
                print()
                while percent >= 0.2:
                    print(second)
                    time.sleep(1)
                    print(third)
                    time.sleep(1)
                    print(percent, '%')
                    time.sleep(1)
                    print()
                    message = 'Первая пара: USDCUSDT ' + str(
                        first) + '\nВторая пара: ' + symbol + 'USDC ' + str(
                        second) + '\nТретья пара: ' + symbol + 'USDT ' + str(third) + '\nПроцент: ' + str(percent)
                    print(requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=5772771813&text=' + message))
                    print(requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message))
                    print(requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=808632051&text=' + message))
                    first, second, third = get_prices(symbol)
                    time.sleep(5)
                    percent = (first / second * third - 1) * 100
                first, second, third = get_prices(symbol)
                percent = (second / first / third - 1)
                print(symbol)
                print(second)
                print(third)
                print(percent, '%')
                print()
                while percent >= 0.2:
                    print(second)
                    time.sleep(1)
                    print(third)
                    time.sleep(1)
                    print(percent, '%')
                    time.sleep(1)
                    print()
                    message = 'Первая пара: '+symbol+'USDT '+str(second)+'\nВторая пара: '+symbol+'USDC '+str(third)+'\nТретья пара: USDCUSDT '+str(first)+'\nПроцент: '+str(percent)
                    print(requests.get('https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=5772771813&text=' + message))
                    print(requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message))
                    first, second, third = get_prices(symbol)
                    percent = (second / first / third - 1)
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])


if __name__ == '__main__':
    p = Process(target=start, args=(symbols_1,))
    p1 = Process(target=start, args=(symbols_2,))
    p2 = Process(target=start, args=(symbols_3,))
    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()

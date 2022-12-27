import sys
import time
from kucoin.client import Client
from multiprocessing import Process
import requests
api_key = '63a17825b0ba7800018ae437'
api_secret = 'a09735c0-e74f-41b2-b2c0-39a443939c15'
api_passphrase = 'DAvid140405'
client = Client(api_key, api_secret, api_passphrase)

symbols_1 = ['TRX', 'ATOM', 'DOT', 'TRX', 'NEO', 'AVAX', 'ADA', 'VET', 'MIR', 'NEO', 'AAVE']
symbols_2 = ['SOL', 'NEAR', 'LUNA', 'LINK', 'JASMY', 'BCH', 'KCS', 'GMT', 'ACQ', 'DASH', 'VRA']
symbols_3 = ['ETC', 'HFT', 'LTC', 'ZEC', 'APE', 'RUNE', 'BNB', 'EOS', 'FTM', 'MJT', 'OP', 'XLM']
stables = ['USDC', 'KCS']



def start(crypto_symbol):
    while True:
        try:
            for symbol in crypto_symbol:
                for stable in stables:
                    first = float(client.get_ticker(stable+'-USDT')['price'])
                    second = float(client.get_ticker(symbol+'-USDT')['price'])
                    third = float(client.get_ticker(symbol+'-'+stable)['price'])
                    percent = (first / second * third - 1) * 100 - 0.3
                    print(symbol, stable)
                    print(second)
                    print(third)
                    print(percent, '%')
                    print()
                    while percent >= 0.1:
                        print(second)
                        time.sleep(1)
                        print(third)
                        time.sleep(1)
                        print(percent, '%')
                        time.sleep(1)
                        print()
                        message = 'Первая пара: '+stable+'USDT '+str(first)+'\nВторая пара: '+symbol+stable+' '+str(second)+'\nТретья пара: '+symbol+'USDT '+str(third)+'\nПроцент: '+str(percent)
                        print(requests.get('https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=5772771813&text=' + message))
                        print(requests.get(
                            'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message))
                        first = float(client.get_ticker(stable + '-USDT')['price'])
                        second = float(client.get_ticker(symbol + '-USDT')['price'])
                        third = float(client.get_ticker(symbol + '-' + stable)['price'])
                        percent = (first / second * third - 1) * 100 - 0.3
                    first = float(client.get_ticker(stable + '-USDT')['price'])
                    second = float(client.get_ticker(symbol + '-USDT')['price'])
                    third = float(client.get_ticker(symbol + '-' + stable)['price'])
                    percent = (100 / third * second / first - 100) - 0.3
                    print(symbol, stable)
                    print(second)
                    print(third)
                    print(percent, '%')
                    print()
                    while percent >= 0.1:
                        print(second)
                        time.sleep(1)
                        print(third)
                        time.sleep(1)
                        print(percent, '%')
                        time.sleep(1)
                        print()
                        message = 'Первая пара: '+symbol+'USDT '+str(third)+'\nВторая пара: '+symbol+stable+' '+str(second)+'\nТретья пара: '+stable+'USDT '+str(first)+'\n Процент: '+str(percent)
                        print(requests.get('https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=5772771813&text=' + message))
                        print(requests.get(
                            'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message))
                        first = float(client.get_ticker(stable + '-USDT')['price'])
                        second = float(client.get_ticker(symbol + '-USDT')['price'])
                        third = float(client.get_ticker(symbol + '-' + stable)['price'])
                        percent = (100 / third * second / first - 100) - 0.3
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])


if __name__ == '__main__':
    p = Process(target=start, args=(symbols_1, ))
    p1 = Process(target=start, args=(symbols_2,))
    p2 = Process(target=start, args=(symbols_3,))
    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()

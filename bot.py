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

symbols_1 = ['TRX', 'DOT', 'TRX', 'AVAX', 'ADA', 'SAND', 'CHZ']
symbols_2 = ['SOL', 'LINK', 'GMT', 'OP', 'BIT', 'LDO', 'MATIC', 'APEX']
symbols_3 = ['HFT', 'LTC', 'APE', 'EOS', 'XLM', 'MANA', 'OKSE']
qty = 12.0


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
    return [float(priceusd), float(priceusdc), float(priceusdt)]


def get_balance(coin):
    balances = session.get_wallet_balance()['result']['balances']
    for balance in balances:
        if balance['coin'] == coin:
            return float(balance['free'])
            break
def bybys(symbol):
  session.place_active_order(
                                symbol="USDCUSDT",
                                side="Buy",
                                type="MARKET",
                                qty=qty,
                                timeInForce="GTC"
  )
  qty1 = int(get_balance('USDC') * 10000) / 10000
  session.place_active_order(
                                symbol=symbol + "USDC",
                                side="Buy",
                                type="MARKET",
                                qty=qty1,
                                timeInForce="GTC"
  )
  qty2 = get_balance(symbol)
  session.place_active_order(
                                symbol=symbol + "USDT",
                                side="Sell",
                                type="MARKET",
                                qty=qty2,
                                timeInForce="GTC"
  )
def ssby(symbol):
  session.place_active_order(
                            symbol=symbol + "USDT",
                            side="Buy",
                            type="MARKET",
                            qty=qty,
                            timeInForce="GTC"
  )
  qty1 = get_balance(symbol)
  session.place_active_order(
                            symbol=symbol + "USDC",
                            side="Sell",
                            type="MARKET",
                            qty=qty1,
                            timeInForce="GTC"
  )
  qty2 = int(get_balance('USDC') * 100) / 100
  session.place_active_order(
                            symbol="USDCUSDT",
                            side="Sell",
                            type="MARKET",
                            qty=qty2,
                            timeInForce="GTC"
  )

def start(crypto_symbol):
    while True:
        try:
            for symbol in crypto_symbol:
                time.sleep(1)
                #start_balance = get_balance('USDT')
                first, second, third = get_prices(symbol)
                percent = (third / second - 1) * 100
                print(symbol)
                print(third,'USDT')
                print(second,'USDC')
                print(percent)
                while percent >= 1.5:
                    #bybys(symbol)
                    print(symbol)
                    print(third,'USDT')
                    print(second,'USDC')
                    print(percent)
                    message = symbol+'USDT->'+symbol+'USDC->'+'USDCUSDT\nUSDT '+str(third)+'\nUSDC '+str(second)
                    print(message)
                    #end_balance = get_balance('USDT')
                    #message = 'Начальный баланс: ' + str(start_balance) + '\n' + message + '\nКонечный баланс: ' + str(end_balance)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=5772771813&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message)
                    first, second, third = get_prices(symbol)
                    percent = (second / third - 1) * 100
                    #start_balance = end_balance
                    time.sleep(3)
                percent = (second / third - 1) * 100
                print(symbol)
                print(third,'USDT')
                print(second,'USDC')
                print(percent)
                while percent >= 1.5:
                    #bybys(symbol)
                    print(symbol)
                    print(third,'USDT')
                    print(second,'USDC')
                    print(percent)
                    message = 'USDCUSDT->'+symbol+'USDC->'+symbol+'USDT\nUSDT '+str(third)+'\nUSDC '+str(second)
                    print(message)
                    #end_balance = get_balance('USDT')
                    #message = 'Начальный баланс: ' + str(start_balance) + '\n' + message + '\nКонечный баланс: ' + str(end_balance)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=5772771813&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message)
                    first, second, third = get_prices(symbol)
                    percent = (second / third - 1) * 100
                    #start_balance = end_balance
                    time.sleep(3)
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])
            print(symbol)
            if e.args[0] != 'float division by zero':
                print(requests.get(
                  'https://api.telegram.org/bot5891493576:AAHdHerlKmRkmUHW_CxNKL4MXg6e3ebBaGw/sendMessage?chat_id=400635213&text=' + str(
                e.args[0])))

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

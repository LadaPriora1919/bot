import sys
from multiprocessing import Process
import requests
import time
from google_sheets_write import write
from binance.client import Client

client = Client("ctzxM8oSIrGjUEMoHCU8HHuiihuIu5yk9f3bMbXYiDPx0AZGzYzjENXcCI6fJBj0", "GmpusN6lU1d2bENdlmKs040XVweVwDxQh864Z4oAZm32GSjHhH0k3S2gZMdBwsP3")
client1 = Client("rH3BUXBHPQvUjD2Tc8C9CIFwMefyjAZuWqrVfwMIK4AHPWqkvgFU1D9Lt9ScSyes", "shZSn8rQaoUxQ3i2t0KtMCySc4BtIPTkWvkKI4BdQBLHGKZzwYsOXkzMnhUHnDAn")

qty = 12.0
different_dict = {'MASK': 0.001, 'ANT': 0.001, 'MTL': 0.001, 'DYDX': 0.001, 'KNC': 0.001, 'ZIL': 0.00001, 'GMT': 0.0001, 'UNI': 0.001, 'FTM': 0.0001, 'WAVES': 0.001, 'LDO': 0.001, 'FIL': 0.001, 'DOT': 0.001, 'GAL': 0.001, 'APE': 0.001, 'NEAR': 0.001, 'SOL': 0.01, 'MATIC': 0.0001, 'KAVA': 0.001, 'DOGE': 0.00001, 'LINK': 0.001, 'VET': 0.00001, 'DASH': 0.01, 'BNB': 0.1, 'ACH': 0.00001, '1INCH': 0.001, 'AAVE': 0.1, 'BCH': 0.1, 'LTC': 0.01, 'XRP': 0.0001, 'ETC': 0.01, 'ADA': 0.0001, 'EOS': 0.001, 'TRX': 0.00001}

symbols_1 = ['BNB', '1INCH', 'BCH', 'LTC', 'VET', 'KAVA', 'NEAR', 'DOT', 'WAVES', 'KNC', 'DYDX']
symbols_2 = ['ACH', 'XRP', 'ETC', 'DASH', 'LINK', 'MATIC', 'APE', 'FIL', 'FTM', 'ZIL', 'MTL']
symbols_3 = ['ADA', 'AAVE', 'EOS', 'TRX', 'DOGE', 'SOL', 'GAL', 'LDO', 'UNI', 'GMT', 'ANT', 'MASK']


def bybys(symbol):
    client1.create_order(
                                symbol="BUSDUSDT",
                                side="BUY",
                                type="MARKET",
                                quantity=qty,
                                timeInForce="GTC"
    )
    qty1 = int(client1.get_asset_balance(asset='BUSD')['free'] * 10000) / 10000
    client1.create_order(
                                symbol=symbol + "BUSD",
                                side="BUY",
                                type="MARKET",
                                quantity=qty1,
                                timeInForce="GTC"
    )
    qty2 = client1.get_asset_balance(asset=symbol)['free']
    client1.create_order(
                                symbol=symbol + "USDT",
                                side="SELL",
                                type="MARKET",
                                quantity=qty2,
                                timeInForce="GTC"
  )


def ssby(symbol):
    print(client1.create_order(
                            symbol=symbol + "USDT",
                            side="BUY",
                            type="MARKET",
                            quantity=qty,
                            timeInForce="GTC"
    ))
    qty1 = client1.get_asset_balance(asset=symbol)['free']
    print(client1.create_order(
                            symbol=symbol + "BUSD",
                            side="SELL",
                            type="MARKET",
                            quantity=qty1,
                            timeInForce="GTC"
    ))
    qty2 = int(client1.get_asset_balance(asset='BUSD')['free'] * 100) / 100
    print(client1.create_order(
                            symbol="BUSDUSDT",
                            side="SELL",
                            type="MARKET",
                            quantity=qty2,
                            timeInForce="GTC"
    ))


def get_prices(crypto):
    priceusdt = client.get_ticker(symbol=crypto+'USDT')['lastPrice']
    priceusdc = client.get_ticker(symbol=crypto+'BUSD')['lastPrice']
    priceusd = client.get_ticker(symbol='BUSDUSDT')['lastPrice']
    return [float(priceusd), float(priceusdc), float(priceusdt)]


def start(crypto_symbol):
    while True:
        try:
            for symbol in crypto_symbol:
                time.sleep(1)
                start_balance = client1.get_asset_balance(asset='USDT')['free']
                first, second, third = get_prices(symbol)
                percent = ((second - different_dict[symbol]) / (third + different_dict[symbol]) - 1) * 100 - 0.3
                print(symbol)
                print(third + different_dict[symbol],'USDT')
                print(second - different_dict[symbol],'BUSD')
                print(percent)
                while percent >= 0.1:
                    #ssby(symbol)
                    print(symbol)
                    print(third + different_dict[symbol],'USDT')
                    print(second - different_dict[symbol],'BUSD')
                    print(percent)
                    end_balance = client1.get_asset_balance(asset='USDT')['free']
                    message = 'Начальный баланс: ' + start_balance + '\n' + symbol+'USDT->'+symbol+'BUSD->'+'BUSDUSDT\nUSDT '+str(third + different_dict[symbol])+'\nBUSD '+str(second- different_dict[symbol]) + '\nПрофит ' + str(percent) + '\nКонечный баланс: ' + end_balance
                    print(message)
                    write(symbol, third  + different_dict[symbol], second - different_dict[symbol], percent, start_balance, end_balance)
                    requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=400635213&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=808632051&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message)
                    start_balance = end_balance
                    first, second, third = get_prices(symbol)
                    percent = ((second - different_dict[symbol]) / (third + different_dict[symbol]) - 1) * 100 - 0.3
                percent = ((third - different_dict[symbol]) / (second + different_dict[symbol]) - 1) * 100 - 0.3
                print(symbol)
                print(third - different_dict[symbol], 'USDT')
                print(second + different_dict[symbol], 'BUSD')
                print(percent)
                while percent >= 0.1:
                    #bybys(symbol)
                    print(symbol)
                    print(third - different_dict[symbol], 'USDT')
                    print(second + different_dict[symbol], 'BUSD')
                    print(percent)
                    end_balance = client1.get_asset_balance(asset='USDT')['free']
                    message = 'Начальный баланс: ' + start_balance + '\nBUSDUSDT->' + symbol + 'BUSD->' + symbol + 'USDT\nUSDT ' + str(
                            third - different_dict[symbol]) + '\nBUSD ' + str(second + different_dict[symbol]) + '\nПрофит ' + str(percent) + '\nКонечный баланс: ' + end_balance
                    print(message)
                    write(symbol, third - different_dict[symbol], second + different_dict[symbol], percent, start_balance, end_balance)
                    requests.get(
                            'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=400635213&text=' + message)
                    requests.get(
                            'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=808632051&text=' + message)
                    requests.get(
                            'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message)
                    start_balance = end_balance
                    first, second, third = get_prices(symbol)
                    percent = ((third - different_dict[symbol]) / (second + different_dict[symbol]) - 1) * 100 - 0.3

        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])
            print(symbol)
            if e.args[0] != 'float division by zero':
                print(requests.get(
                  'https://api.telegram.org/bot5891493576:AAHdHerlKmRkmUHW_CxNKL4MXg6e3ebBaGw/sendMessage?chat_id=400635213&text=' + 'binance\n' +str(
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

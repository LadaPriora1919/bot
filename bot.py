import sys
from multiprocessing import Process
import requests
import time
from google_sheets_write import write
from binance.client import Client

client = Client("ctzxM8oSIrGjUEMoHCU8HHuiihuIu5yk9f3bMbXYiDPx0AZGzYzjENXcCI6fJBj0", "GmpusN6lU1d2bENdlmKs040XVweVwDxQh864Z4oAZm32GSjHhH0k3S2gZMdBwsP3")
client1 = Client("rH3BUXBHPQvUjD2Tc8C9CIFwMefyjAZuWqrVfwMIK4AHPWqkvgFU1D9Lt9ScSyes", "shZSn8rQaoUxQ3i2t0KtMCySc4BtIPTkWvkKI4BdQBLHGKZzwYsOXkzMnhUHnDAn")

symbols_1 = ['1INCH', 'AAVE', 'ACM', 'ADA', 'ALGO', 'ALICE', 'ALPACA', 'ALPHA', 'ANT', 'AR', 'ASR', 'ATA', 'ATM', 'ATOM', 'AUDIO', 'AUD', 'AUTO', 'AVA', 'AVAX', 'AXS', 'BADGER', 'BAKE', 'BAL', 'BAND', 'BAT', 'BCH', 'BEL', 'BLZ', 'BNT', 'BOND', 'BURGER', 'C98', 'CAKE', 'CELO', 'CFX', 'CHR', 'CHZ', 'COCOS', 'COMP', 'COTI', 'CRV', 'CTK', 'CTSI', 'CTXC', 'DASH', 'DEGO', 'DEXE', 'DIA', 'DODO', 'DOT', 'DREP', 'DUSK', 'EGLD', 'ENJ', 'EOS', 'ERN', 'ETC', 'EUR', 'FARM', 'FET', 'FIL', 'FIO', 'FIRO', 'FIS', 'FLOW', 'FORTH', 'FTM', 'GBP', 'GRT', 'GTC', 'HARD', 'HBAR', 'HIVE', 'ICP', 'ICX', 'INJ', 'IOTA', 'JUV', 'KAVA', 'KLAY', 'KNC', 'KSM', 'LINK', 'LIT', 'LPT', 'LRC', 'LSK', 'LTC', 'LTO', 'LUNA', 'MANA', 'MASK', 'MATIC', 'MDX', 'MINA', 'MKR', 'MLN', 'MTL', 'NEAR']
symbols_2 = ['NEO', 'NMR', 'NULS', 'OCEAN', 'OGN', 'OG', 'OMG', 'OM', 'ONT', 'ORN', 'OXT', 'PAXG', 'PHA', 'POLS', 'PSG', 'PUNDIX', 'QNT', 'QTUM', 'QUICK', 'RAY', 'RUNE', 'SAND', 'SFP', 'SNX', 'SOL', 'STORJ', 'STRAX', 'STX', 'SUPER', 'SUSHI', 'SXP', 'TFUEL', 'THETA', 'TKO', 'TOMO', 'TRB', 'TVK', 'TWT', 'UMA', 'UNFI', 'UNI', 'UTK', 'WAVES', 'WING', 'WRX', 'XLM', 'XMR', 'XRP', 'XTZ', 'XVS', 'YFI', 'ZEC', 'ZEN', 'ZRX', 'BNB', 'ETH', 'NKN', 'BAR', 'MBOX', 'REQ', 'GHST', 'WAXP', 'ELF', 'DYDX', 'ILV', 'YGG', 'SYS', 'DF', 'FIDA', 'FRONT', 'CVP', 'AGLD', 'RAD', 'RARE', 'LAZIO', 'CHESS', 'ADX', 'AUCTION', 'BNX', 'MOVR', 'CITY', 'ENS', 'KP3R', 'PORTO', 'POWR', 'PLA', 'PYR', 'RNDR', 'ALCX', 'SANTOS', 'MC', 'BICO', 'FLUX', 'FXS', 'VOXEL', 'HIGH', 'CVX', 'JOE', 'IMX', 'GLMR']
symbols_3 = ['LOKA', 'SCRT', 'API3', 'ACA', 'XNO', 'WOO', 'ALPINE', 'T', 'ASTR', 'GMT', 'KDA', 'APE', 'BSW', 'BIFI', 'MULTI', 'STEEM', 'MOB', 'NEXO', 'REI', 'GAL', 'LDO', 'OP', 'STG', 'GMX', 'NEBL', 'POLYX', 'APT', 'OSMO', 'HFT', 'PHB', 'HOOK', 'MAGIC']
qty = 12.0
different_dict = {'1INCH': 0.001, 'AAVE': 0.1, 'ACM': 0.001, 'ADA': 0.0001, 'ALGO': 0.0001, 'ALICE': 0.001, 'ALPACA': 0.0001, 'ALPHA': 0.0001, 'ANT': 0.001, 'AR': 0.01, 'ASR': 0.001, 'ATA': 0.0001, 'ATM': 0.01, 'ATOM': 0.001, 'AUDIO': 0.0001, 'AUD': 0.0001, 'AUTO': 0.1, 'AVA': 0.001, 'AVAX': 0.01, 'AXS': 0.01, 'BADGER': 0.01, 'BAKE': 0.0001, 'BAL': 0.001, 'BAND': 0.001, 'BAT': 0.0001, 'BCH': 0.1, 'BEL': 0.001, 'BLZ': 0.0001, 'BNT': 0.001, 'BOND': 0.001, 'BURGER': 0.001, 'C98': 0.0001, 'CAKE': 0.001, 'CELO': 0.001, 'CFX': 0.0001, 'CHR': 0.0001, 'CHZ': 0.0001, 'COCOS': 0.0001, 'COMP': 0.01, 'COTI': 0.0001, 'CRV': 0.001, 'CTK': 0.001, 'CTSI': 0.0001, 'CTXC': 0.0001, 'DASH': 0.01, 'DEGO': 0.001, 'DEXE': 0.001, 'DIA': 0.001, 'DODO': 0.0001, 'DOT': 0.001, 'DREP': 0.0001, 'DUSK': 0.0001, 'EGLD': 0.01, 'ENJ': 0.0001, 'EOS': 0.001, 'ERN': 0.001, 'ETC': 0.01, 'EUR': 0.0001, 'FARM': 0.1, 'FET': 0.0001, 'FIL': 0.001, 'FIO': 0.0001, 'FIRO': 0.001, 'FIS': 0.0001, 'FLOW': 0.001, 'FORTH': 0.01, 'FTM': 0.0001, 'GBP': 0.001, 'GRT': 0.0001, 'GTC': 0.001, 'HARD': 0.0001, 'HBAR': 0.0001, 'HIVE': 0.0001, 'ICP': 0.001, 'ICX': 0.0001, 'INJ': 0.001, 'IOTA': 0.0001, 'JUV': 0.01, 'KAVA': 0.001, 'KLAY': 0.0001, 'KNC': 0.001, 'KSM': 0.01, 'LINK': 0.001, 'LIT': 0.001, 'LPT': 0.01, 'LRC': 0.0001, 'LSK': 0.001, 'LTC': 0.01, 'LTO': 0.0001, 'LUNA': 0.0001, 'MANA': 0.0001, 'MASK': 0.001, 'MATIC': 0.0001, 'MDX': 0.0001, 'MINA': 0.001, 'MKR': 1, 'MLN': 0.01, 'MTL': 0.001, 'NEAR': 0.001, 'NEO': 0.01, 'NMR': 0.01, 'NULS': 0.0001, 'OCEAN': 0.0001, 'OGN': 0.0001, 'OG': 0.001, 'OMG': 0.001, 'OM': 0.0001, 'ONT': 0.0001, 'ORN': 0.001, 'OXT': 0.0001, 'PAXG': 1, 'PHA': 0.0001, 'POLS': 0.001, 'PSG': 0.01, 'PUNDIX': 0.001, 'QNT': 0.1, 'QTUM': 0.001, 'QUICK': 0.1, 'RAY': 0.0001, 'RUNE': 0.001, 'SAND': 0.0001, 'SFP': 0.0001, 'SNX': 0.001, 'SOL': 0.01, 'STORJ': 0.0001, 'STRAX': 0.001, 'STX': 0.001, 'SUPER': 0.0001, 'SUSHI': 0.001, 'SXP': 0.0001, 'TFUEL': 0.0001, 'THETA': 0.001, 'TKO': 0.0001, 'TOMO': 0.0001, 'TRB': 0.01, 'TVK': 0.0001, 'TWT': 0.0001, 'UMA': 0.001, 'UNFI': 0.001, 'UNI': 0.001, 'UTK': 0.0001, 'WAVES': 0.001, 'WING': 0.01, 'WRX': 0.0001, 'XLM': 0.0001, 'XMR': 0.1, 'XRP': 0.0001, 'XTZ': 0.001, 'XVS': 0.01, 'YFI': 1, 'ZEC': 0.1, 'ZEN': 0.01, 'ZRX': 0.0001, 'BNB': 0.1, 'ETH': 0.01, 'NKN': 0.0001, 'BAR': 0.01, 'MBOX': 0.001, 'REQ': 0.0001, 'GHST': 0.001, 'WAXP': 0.0001, 'ELF': 0.0001, 'DYDX': 0.001, 'ILV': 0.01, 'YGG': 0.0001, 'SYS': 0.0001, 'DF': 0.0001, 'FIDA': 0.0001, 'FRONT': 0.0001, 'CVP': 0.0001, 'AGLD': 0.001, 'RAD': 0.001, 'RARE': 0.0001, 'LAZIO': 0.0001, 'CHESS': 0.001, 'ADX': 0.0001, 'AUCTION': 0.01, 'BNX': 0.1, 'MOVR': 0.01, 'CITY': 0.01, 'ENS': 0.01, 'KP3R': 0.01, 'PORTO': 0.0001, 'POWR': 0.0001, 'PLA': 0.001, 'PYR': 0.01, 'RNDR': 0.001, 'ALCX': 0.1, 'SANTOS': 0.001, 'MC': 0.001, 'BICO': 0.001, 'FLUX': 0.001, 'FXS': 0.001, 'VOXEL': 0.0001, 'HIGH': 0.001, 'CVX': 0.001, 'JOE': 0.0001, 'IMX': 0.001, 'GLMR': 0.0001, 'LOKA': 0.0001, 'SCRT': 0.001, 'API3': 0.001, 'ACA': 0.0001, 'XNO': 0.001, 'WOO': 0.0001, 'ALPINE': 0.0001, 'T': 0.0001, 'ASTR': 0.0001, 'GMT': 0.0001, 'KDA': 0.001, 'APE': 0.001, 'BSW': 0.0001, 'BIFI': 0.1, 'MULTI': 0.01, 'STEEM': 0.0001, 'MOB': 0.001, 'NEXO': 0.001, 'REI': 0.0001, 'GAL': 0.001, 'LDO': 0.001, 'OP': 0.001, 'STG': 0.0001, 'GMX': 0.01, 'NEBL': 0.001, 'POLYX': 0.0001, 'APT': 0.0001, 'OSMO': 0.001, 'HFT': 0.0001, 'PHB': 0.0001, 'HOOK': 0.0001, 'MAGIC': 0.0001}

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
                while percent >= 0.05:
                    #ssby(symbol)
                    print(symbol)
                    print(third + different_dict[symbol],'USDT')
                    print(second - different_dict[symbol],'BUSD')
                    print(percent)
                    end_balance = client1.get_asset_balance(asset='USDT')['free']
                    message = 'Начальный баланс: ' + start_balance + '\n' + symbol+'USDT->'+symbol+'BUSD->'+'BUSDUSDT\nUSDT '+str(third + different_dict[symbol])+'\nBUSD '+str(second- different_dict[symbol]) + '\nПрофит ' + str(percent) + '\nКонечный баланс: ' + end_balance
                    print(message)
                    write(symbol, third  + different_dict[symbol], second - different_dict[symbol], percent)
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
                    write(symbol, third - different_dict[symbol], second + different_dict[symbol], percent)
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

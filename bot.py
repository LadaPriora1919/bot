import sys
from multiprocessing import Process
import requests
import time
from google_sheets_write import write
from binance.client import Client

client = Client("ctzxM8oSIrGjUEMoHCU8HHuiihuIu5yk9f3bMbXYiDPx0AZGzYzjENXcCI6fJBj0", "GmpusN6lU1d2bENdlmKs040XVweVwDxQh864Z4oAZm32GSjHhH0k3S2gZMdBwsP3")

symbols_1 = ['1INCH', 'AAVE', 'ACM', 'ADA', 'AKRO', 'ALGO', 'ALICE', 'ALPACA', 'ALPHA', 'ANKR', 'ANT', 'ARPA', 'AR', 'ASR', 'ATA', 'ATM', 'ATOM', 'AUDIO', 'AUD', 'AUTO', 'AVA', 'AVAX', 'AXS', 'BADGER', 'BAKE', 'BAL', 'BAND', 'BAT', 'BCH', 'BEL', 'BLZ', 'BNT', 'BOND', 'BURGER', 'C98', 'CAKE', 'CELO', 'CELR', 'CFX', 'CHR', 'CHZ', 'CKB', 'CLV', 'COCOS', 'COMP', 'COS', 'COTI', 'CRV', 'CTK', 'CTSI', 'CTXC', 'DASH', 'DATA', 'DEGO', 'DENT', 'DEXE', 'DGB', 'DIA', 'DOCK', 'DODO', 'DOGE', 'DOT', 'DREP', 'DUSK', 'EGLD', 'ENJ', 'EOS', 'ERN', 'ETC', 'EUR', 'FARM', 'FET', 'FIL', 'FIO', 'FIRO', 'FIS', 'FLOW', 'FORTH', 'FTM', 'GBP', 'GRT', 'GTC', 'HARD', 'HBAR', 'HIVE', 'HOT', 'ICP', 'ICX', 'INJ', 'IOST', 'IOTA', 'IOTX', 'JST', 'JUV', 'KAVA', 'KEY', 'KLAY', 'KNC']
symbols_2 = ['KSM', 'LINA', 'LINK', 'LIT', 'LPT', 'LRC', 'LSK', 'LTC', 'LTO', 'LUNA', 'MANA', 'MASK', 'MATIC', 'MBL', 'MDT', 'MDX', 'MINA', 'MKR', 'MLN', 'MTL', 'NEAR', 'NEO', 'NMR', 'NULS', 'OCEAN', 'OGN', 'OG', 'OMG', 'OM', 'ONE', 'ONT', 'ORN', 'OXT', 'PAXG', 'PERP', 'PHA', 'POLS', 'POND', 'PSG', 'PUNDIX', 'QNT', 'QTUM', 'QUICK', 'RAY', 'REEF', 'ROSE', 'RSR', 'RUNE', 'RVN', 'SAND', 'SC', 'SFP', 'SKL', 'SLP', 'SNX', 'SOL', 'STMX', 'STORJ', 'STPT', 'STRAX', 'STX', 'SUN', 'SUPER', 'SUSHI', 'SXP', 'TFUEL', 'THETA', 'TKO', 'TLM', 'TOMO', 'TRB', 'TROY', 'TRX', 'TVK', 'TWT', 'UMA', 'UNFI', 'UNI', 'UTK', 'VET', 'VITE', 'WAVES', 'WING', 'WRX', 'XLM', 'XMR', 'XRP', 'XTZ', 'XVG', 'XVS', 'YFI', 'ZEC', 'ZEN', 'ZIL', 'ZRX', 'REN']
symbols_3 = ['NKN', 'BAR', 'MBOX', 'FOR', 'REQ', 'GHST', 'WAXP', 'ELF', 'DYDX', 'IDEX', 'VIDT', 'GALA', 'ILV', 'YGG', 'SYS', 'DF', 'FIDA', 'FRONT', 'CVP', 'AGLD', 'RAD', 'BETA', 'RARE', 'LAZIO', 'CHESS', 'ADX', 'AUCTION', 'DAR', 'BNX', 'MOVR', 'CITY', 'ENS', 'KP3R', 'QI', 'PORTO', 'POWR', 'JASMY', 'AMP', 'PLA', 'PYR', 'RNDR', 'ALCX', 'SANTOS', 'MC', 'BICO', 'FLUX', 'FXS', 'VOXEL', 'HIGH', 'CVX', 'PEOPLE', 'OOKI', 'SPELL', 'JOE', 'ACH', 'IMX', 'GLMR', 'LOKA', 'SCRT', 'API3', 'ACA', 'XNO', 'WOO', 'ALPINE', 'T', 'ASTR', 'GMT', 'KDA', 'APE', 'BSW', 'BIFI', 'MULTI', 'STEEM', 'MOB', 'NEXO', 'REI', 'GAL', 'LDO', 'EPX', 'OP', 'LEVER', 'STG', 'LUNC', 'GMX', 'NEBL', 'POLYX', 'APT', 'OSMO', 'HFT', 'PHB', 'HOOK', 'MAGIC']
qty = 12.0


def get_prices(crypto):
    priceusdt = client.get_ticker(symbol=crypto+'USDT')['lastPrice']
    priceusdc = client.get_ticker(symbol=crypto+'BUSD')['lastPrice']
    priceusd = client.get_ticker(symbol='BUSDUSDT')['lastPrice']
    return [float(priceusd), float(priceusdc), float(priceusdt)]

def start(crypto_symbol):
    while True:
        time.sleep(0.5)
        try:
            for symbol in crypto_symbol:
                first, second, third = get_prices(symbol)
                percent = (second / third - 1) * 100 - 0.3
                print(symbol)
                print(third,'USDT')
                print(second,'BUSD')
                print(percent)
                while percent >= 0.5:
                    print(symbol)
                    print(third,'USDT')
                    print(second,'BUSD')
                    print(percent)
                    message = symbol+'USDT->'+symbol+'BUSD->'+'BUSDUSDT\nUSDT '+str(third)+'\nBUSD '+str(second) + '\nПрофит ' + str(percent)
                    print(message)
                    write(symbol, third, second, percent)
                    requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=400635213&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=808632051&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message)
                    first, second, third = get_prices(symbol)
                    percent = (second / third - 1) * 100 - 0.3
                    time.sleep(3)
                percent = (third / second - 1) * 100 - 0.3
                print(symbol)
                print(third,'USDT')
                print(second,'BUSD')
                print(percent)
                while percent >= 0.5:
                    print(symbol)
                    print(third,'USDT')
                    print(second,'BUSD')
                    print(percent)
                    write(symbol, third, second, percent)
                    message = 'BUSDUSDT->'+symbol+'BUSD->'+symbol+'USDT\nUSDT '+str(third)+'\nBUSD '+str(second) + '\nПрофит ' + str(percent)
                    print(message)
                    requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=400635213&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5641617419:AAH7sGmzV4D6JM5VA__dbeWc5ZHp07SWlZY/sendMessage?chat_id=808632051&text=' + message)
                    requests.get(
                        'https://api.telegram.org/bot5814069489:AAEkWaGh5kaWePUH6vCyf_cCAeKQd_GO30M/sendMessage?chat_id=355611262&text=' + message)
                    first, second, third = get_prices(symbol)
                    percent = (third / second - 1) * 100 - 0.3
                    time.sleep(3)
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

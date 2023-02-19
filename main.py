import time

from telethon.sync import TelegramClient, events
from binance.client import Client
from telethon.tl.types import PeerChannel
from google_sheets_write import write
client_binance = Client('ejOiO2UMdeYxH399CzbgMlfnGxt1PhPH6uQfsrAC388W1suiLmz1pSBkD7CNiwhj', 'OZKGFKWoTZgmBzNKVipxswiL8idgUPBzUH87idZlPEK3THdNZiZA7mbyec30w8su', tld='com', testnet=False)
api_id = 23737826
api_hash = 'd010cb09043b330dc92a4599882594b9'
client = TelegramClient('session_name', api_id, api_hash)
order_dict = {}
client.API_URL = 'https://api.binance.com/api'


def get_precision(symbol):
    info = client_binance.futures_exchange_info()
    for x in info['symbols']:
        if x['symbol'] == symbol:
            return x['quantityPrecision']


def search_coin(message):
    message = message[message.find('\n'):message.rfind('\n')]
    coin = message[message.find('\n'):message.rfind('\n')].replace('Монета:', '').replace('▪', '').replace(' ', '').replace(' ', '\n') + 'USDT'
    return coin.replace(' ', '')


def bot_open_order(side, coin):
    if float(client_binance.futures_position_information(symbol=coin)[0]['positionAmt']) == 0:
        price = float(client_binance.futures_symbol_ticker(symbol=coin)['price'])
        order_id = client_binance.futures_create_order(
                                            symbol=coin,
                                            side=side,
                                            type='MARKET',
                                            quantity=float(round(50 / price, get_precision(coin))),
                                            leverage=10,
                                            newClientOrderId=coin,
                                            )
        print(order_id)
        order_dict[coin+'side'] = side
        order_dict[coin+'qty'] = order_id['origQty']
        order_dict[coin+'start'] = client_binance.futures_symbol_ticker(symbol=coin)['price']


def bot_cancel_order(coin):
    print(order_dict)
    print(repr(coin))
    side = order_dict[coin+'side']
    if side == 'BUY':
        side1 = 'SELL'
    else:
        side1 = 'BUY'
    print(client_binance.futures_create_order(
                                        symbol=coin,
                                        side=side1,
                                        type='MARKET',
                                        quantity=float(order_dict[coin+'qty']),
                                        leverage=1,
                                        newClientOrderId=coin,
                                        ))
    write('HARDCORE x125', coin, 'Closed', side, str(order_dict[coin+'start']).replace('.', ','), str(client_binance.futures_symbol_ticker(symbol=coin)['price']).replace('.', ','))
    del order_dict[coin+'side']
    del order_dict[coin+'qty']
    del order_dict[coin+'start']


@client.on(events.NewMessage(chats=[PeerChannel(1500109546)]))
async def normal_handler(event):
    print(event)
    message = str(event.message.to_dict()['message'])
    print(message)
    tipe_of_signal = message[0:message.find('\n')]
    tipe_of_signal = tipe_of_signal.replace('📈Тип сигнала:', '').replace(' ', '').replace('🟣', '').replace('🟢', '').replace('🔴', '')
    print(tipe_of_signal[0:7])
    if tipe_of_signal[0:7] == 'Закрыть':
        coin = search_coin(message).replace('️', '').replace('\n', '')
        bot_cancel_order(coin)
    else:
        if tipe_of_signal == 'Шорт':
            side = 'SELL'
        elif tipe_of_signal == 'Лонг':
            side = 'BUY'
        coin = search_coin(message).replace('️', '').replace('\n', '')
        bot_open_order(side, coin)


if __name__ == '__main__':
    while True:
        try:
            client.start()

        except Exception as e:
            print(e, 'error')
            time.sleep(5)
            continue
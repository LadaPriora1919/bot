# coding=utf8
import asyncio
import time
import requests
from telethon.sync import TelegramClient, events
from binance.client import Client
from telethon.tl.types import PeerChannel
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
        time.sleep(2)
        if side == 'BUY':
            stopPrice = round(price * 0.945, get_precision(coin))
            takePrice = round(price * 1.009, get_precision(coin))
            client_binance.futures_create_order(
                symbol=coin,
                side='SELL',
                type='STOP_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=stopPrice)
            client_binance.futures_create_order(
                symbol=coin,
                side='SELL',
                type='TAKE_PROFIT_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=takePrice)
        else:
            stopPrice = round(price * 1.055, get_precision(coin))
            takePrice = round(price * 0.991, get_precision(coin))
            client_binance.futures_create_order(
                symbol=coin,
                side='BUY',
                type='STOP_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=stopPrice)
            client_binance.futures_create_order(
                symbol=coin,
                side='BUY',
                type='TAKE_PROFIT_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=takePrice)
        client.send_message('-1001698890000', coin.replace('USDT') + '\nSide: ' + side + '\nTake profit: ' + str(
            takePrice) + '\nStop Loss: ' + str(stopPrice))


@client.on(events.NewMessage(chats=[PeerChannel(1500109546)]))
async def normal_handler(event):
    message = str(event.message.to_dict()['message'])
    tipe_of_signal = message[0:message.find('\n')]
    tipe_of_signal = tipe_of_signal.replace('📈Тип сигнала:', '').replace(' ', '').replace('🟣', '').replace('🟢', '').replace('🔴', '')
    if tipe_of_signal[0:7] == 'Закрыть':
        pass
    else:
        if tipe_of_signal == 'Шорт':
            side = 'SELL'
        elif tipe_of_signal == 'Лонг':
            side = 'BUY'
        coin = search_coin(message).replace('️', '').replace('\n', '')
        bot_open_order(side, coin)


@client.on(events.NewMessage(chats=[PeerChannel(1266391544)]))
async def normal_handler(event):
    message = str(event.message.to_dict()['message'])
    side = ''
    print(message[0:16])
    print(message[0:18])
    if message[0:16] == '#HANDMADE_SESSION' or message[0:18] == '#BEAUTIFUL_STRATEGY' or message[0:16] == '#SCALPING_session':
        message = message[message.find('\n'):]
        l = message[message.find('#')+1]
        print(message)
        if l == 'S':
            side = 'SELL'
        elif l == 'L':
            side = 'BUY'
        message = message[message.find('#'):]
        coin = message[:message.find('\n')]
        print(coin)
        bot_open_order_cryptonec(message, coin, side)


def bot_open_order_cryptonec(message, coin, side):
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
        message_list = message.split('\n')
        for i in message_list:
            if i[0:13] == 'Take Profit 1:':
                takePrice = round(float(i[i.find(':'):].replace('`', '')), get_precision(coin))
            elif i[0:9] == 'Stop Loss:':
                stopPrice = round(float(i[i.find(':'):].replace('`', '')), get_precision(coin))
        if side == 'BUY':
            client_binance.futures_create_order(
                symbol=coin,
                side='SELL',
                type='STOP_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=stopPrice)
            client_binance.futures_create_order(
                symbol=coin,
                side='SELL',
                type='TAKE_PROFIT_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=takePrice)
        else:
            client_binance.futures_create_order(
                symbol=coin,
                side='BUY',
                type='STOP_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=stopPrice)
            client_binance.futures_create_order(
                symbol=coin,
                side='BUY',
                type='TAKE_PROFIT_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=takePrice)
        client.send_message('-1001698890000', coin.replace('USDT') + '\nSide: ' + side + '\nTake profit: ' + str(
            takePrice) + '\nStop Loss: ' + str(stopPrice))


def trading_coin_find(massage):
    side = ''
    coin = massage[:massage.find(' ')].replace('💲', '').replace('#', '') + "USDT"
    side_l = massage[massage.find('-'):massage.find('\n')]
    if side_l[0] == 'L':
        side = 'BUY'
    elif side_l[0] == 'S':
        side = 'SELL'
    return [coin, side]


def trading_bot_open_poseition(l):
    coin = l[0]
    if float(client_binance.futures_position_information(symbol=coin)[0]['positionAmt']) == 0 and coin != 'BTCUSDT':
        price = float(client_binance.futures_symbol_ticker(symbol=coin)['price'])
        order_id = client_binance.futures_create_order(
            symbol=coin,
            side=l[1],
            type='MARKET',
            quantity=float(round(50 / price, get_precision(coin))),
            leverage=10,
            newClientOrderId=coin,
        )
        time.sleep(2)
        if l[1] == 'BUY':
            stopPrice = round(price * 0.98, get_precision(coin))
            takePrice = round(price * 1.009, get_precision(coin))
            client_binance.futures_create_order(
                symbol=coin,
                side='SELL',
                type='STOP_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=stopPrice)
            client_binance.futures_create_order(
                symbol=coin,
                side='SELL',
                type='TAKE_PROFIT_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=takePrice)
        else:
            stopPrice = round(price * 1.02, get_precision(coin))
            takePrice = round(price * 0.991, get_precision(coin))
            client_binance.futures_create_order(
                symbol=coin,
                side='BUY',
                type='STOP_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=stopPrice)
            client_binance.futures_create_order(
                symbol=coin,
                side='BUY',
                type='TAKE_PROFIT_MARKET',
                timeInForce='GTC',
                quantity=order_id['origQty'],
                stopPrice=takePrice)
        client.send_message('-1001698890000', coin.replace('USDT') +'\nSide: ' + l[1] + '\nTake profit: ' + str(takePrice) + '\nStop Loss: ' + str(stopPrice))


@client.on(events.NewMessage(chats=[PeerChannel(1610165996)]))
async def normal_handler(event):
    print(event)
    message = str(event.message.to_dict()['message'])
    print(message)
    if message.find("Лимитный ордер") == -1 and message[0] == '💲':
        trading_bot_open_poseition(trading_coin_find(message))


if __name__ == '__main__':
    while True:
        try:
            client.start()

        except Exception as e:
            requests.get(
                'https://api.telegram.org/6265786615:AAGc04IPl77A246JW78nXLFMvGaXHDergbY/sendMessage?chat_id=400635213&text=' + e)
            print(e, 'error')
            time.sleep(5)
            continue

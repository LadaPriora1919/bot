from multiprocessing import Process
from get_wallets_tokens import start_analiz
from telegram import bot
from check import check

if __name__ == '__main__':
    p = Process(target=start_analiz)
    p1 = Process(target=bot.polling, kwargs={'none_stop': True, 'interval': 0})
    p2 = Process(target=check)
    p.start()
    p1.start()
    p2.start()
    p.join()
    p1.join()
    p2.join()

from multiprocessing import Process
from get_wallets_tokens import start_analiz
from telegram import telegram_start
from check import check

if __name__ == '__main__':
    p = Process(target=start_analiz)
    print(1)
    p1 = Process(target=telegram_start)
    print(2)
    p2 = Process(target=check)
    print(3)
    p.start()
    print(1)
    p1.start()
    print(2)
    p2.start()
    print(3)
    p.join()
    p1.join()
    p2.join()

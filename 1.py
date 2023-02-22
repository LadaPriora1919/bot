from binance.client import Client
client_binance = Client('ejOiO2UMdeYxH399CzbgMlfnGxt1PhPH6uQfsrAC388W1suiLmz1pSBkD7CNiwhj', 'OZKGFKWoTZgmBzNKVipxswiL8idgUPBzUH87idZlPEK3THdNZiZA7mbyec30w8su', tld='com', testnet=False)

resp = client_binance.c2c

print(resp)
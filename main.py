from binance.client import Client
from binance.enums import *

api_key    = 'TU API KEY'
api_secret = 'TU API SECRET'

client = Client(api_key, api_secret)


cero = 0

while 1 > cero:

#Intentamos comprar
    try:
        eth_price = client.get_symbol_ticker(symbol="BICOUSDT")

        #Calcular compra
        buy_quantity = round(120 / float(eth_price['price']), 2)

        #Compramos
        order = client.create_order(
            symbol='BICOUSDT',
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=buy_quantity)

    except:
        print("No se pudo completar todavía.")
    else:
        cero = 2
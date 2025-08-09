from binance.client import Client
from binance.enums import *
import os
from dotenv import load_dotenv
import logging

load_dotenv()

class TradeBot:
    def __init__(self):
        api_key=os.getenv("API_KEY")
        api_secret=os.getenv("API_SECRET")
        # log in using the api key.
        self.client=Client(api_key,api_secret,testnet=True)
        self.client.FUTURES="https://testnet.binancefuture.com/fapi"

    def place_order(self,symbol,side,type,quantity,price=None,stopprice=None):
        try:
            # Check the order type and places order.
            if type == "MARKET":
                 self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=type,
                    quantity=quantity,
                )

            elif type == "LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=type,
                    quantity=quantity,
                    price=price,
                    timeInForce=TIME_IN_FORCE_GTC
                )
            # third order type
            else :
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP",
                    quantity=quantity,
                    price=price,
                    stopPrice=stopprice,
                    timeInForce=TIME_IN_FORCE_GTC
                )



        except Exception as e:
            logging.exception("Exception while placing order. ")
            return {"error": str(e)}




import websocket
import json
from config import *
import pandas as pd
import csv
from maincrypto import *

#get websocket DATA
def on_open(ws):
    print("opened")
    auth_data = {"action":"auth", "params":"ZwMEsRmpnXsoTtzA2y69x7stNYQ7cY3J"}

    ws.send(json.dumps(auth_data))

    channel_data = {"action":"subscribe", "params":"XA.BTC-USD"}

    ws.send(json.dumps(channel_data))

def on_message(ws, message):
    message = [message]
    data_message = pd.DataFrame(message)
    print(data_message)

socket =  "wss://socket.polygon.io/crypto"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()

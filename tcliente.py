import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
from binance import Client , ThreadedWebsocketManager, ThreadedDepthCacheManager
api_key=os.getenv("BINANCE_API_KEY")
api_secret=os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret)
import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import logger

load_dotenv()

def get_binance_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        logger.error("API credentials missing in .env file.")
        raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET in the .env file.")
    
    logger.info("Initializing Binance Futures Testnet Client.")
    # Initialize client and force testnet
    client = Client(api_key, api_secret, testnet=True)
    return client
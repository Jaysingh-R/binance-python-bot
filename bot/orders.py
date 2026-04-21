from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.client import get_binance_client
from bot.validators import validate_order_input
from bot.logging_config import logger

def place_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    try:
        # 1. Validate
        validate_order_input(symbol, side, order_type, quantity, price)
        
        # 2. Setup Client
        client = get_binance_client()
        
        # 3. Prepare parameters
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity,
        }
        
        if order_type.upper() == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC' # Good Till Cancelled is required for Limit
            
        logger.info(f"Sending {order_type} order request for {quantity} {symbol}: {params}")
        
        # 4. Execute order on futures testnet
        response = client.futures_create_order(**params)
        logger.info(f"Order successful. Response: {response}")
        
        return {"success": True, "data": response}

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e.status_code} - {e.message}")
        return {"success": False, "error": f"API Error: {e.message}"}
    except BinanceRequestException as e:
        logger.error(f"Network error: {e}")
        return {"success": False, "error": "Network connection error."}
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {"success": False, "error": str(e)}
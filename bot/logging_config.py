import logging

def setup_logger():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.DEBUG)
    
    # File handler to generate trading_bot.log
    fh = logging.FileHandler("trading_bot.log")
    fh.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(fh)
        
    return logger

logger = setup_logger()
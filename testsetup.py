import busio
import board

try:
    import adafruit_logging as logging
except:
    import logging
    
try:
    logger = logging.getLogger('test')
except:
    logger = logging.getLogger()

try:
    logging.basicConfig()
except:
    pass

logger.setLevel(logging.DEBUG)

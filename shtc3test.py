from testsetup import *
import adafruit_shtc3

class shtc3test():
    def __init__(self):
        pass
    
    def test(self):
        try:
            i2c = busio.I2C(board.SCL, board.SDA)
        except:
            pass
            """perhaps i2c already initated from another test"""
        
        logger.info("shtc3test: trying adafruit_shtc3.SHTC3(i2c):")
        
        try:
            #with adafruit_shtc3.SHTC3(i2c) as sht:
            """'SHTC3' object has no attribute '__exit__'"""
            sht= adafruit_shtc3.SHTC3(i2c) 
            logger.info("shtc3test: Temperature: "+str(sht.temperature))
            logger.info("shtc3test: Humidity: "+str(sht.relative_humidity))
            logger.info("shtc3test: trying to deinit I2C bus with deinit()")
            i2c.deinit()
            return True
        except:
            logger.info("shtc3test: trying to deinit I2C bus with deinit()")
            i2c.deinit()
            return False

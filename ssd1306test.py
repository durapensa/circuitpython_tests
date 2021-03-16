from testsetup import *
import adafruit_ssd1306

class ssd1306test():
    def __init__(self):
        pass
    
    def test(self):
        try:
            i2c = busio.I2C(board.SCL, board.SDA)
        except:
            pass
            """perhaps i2c already initated from another test"""
        
        logger.info("ssd1306test: trying adafruit_ssd1306.ssd1306(i2c):")
        
        try:
            with adafruit_ssd1306.SSD1306_I2C(128, 64, i2c) as ssd1306:
                logger.info("ssd1306test: Displaying `ssd1306test for 3 seconds, sleeping for 3 seconds")
                oled.fill(0)
                oled.text("ssd1306test", 0,0,1)
                oled.show()
                time.sleep(3)
                oled.fill(0)
                oled.show()
                time.sleep(3)
                logger.info("ssd1306test: trying to deinit I2C bus with deinit()"+str(i2c.deinit()))
                return True
        except:
            logger.info("ssd1306test: trying to deinit I2C bus with deinit()"+str(i2c.deinit()))
            return False

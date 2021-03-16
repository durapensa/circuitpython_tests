from testsetup import *

class i2ctest():
    def __init__(self):
        self.ids = { 
                0x13: 'ppc-daemon', #int  19
                0x3c: 'ssd1306',    #int  60
                0x68: 'rtc-ds1307', #int 104
                0x70: 'shtC3',      #int 112
                0xFF: ''            
              }

    def test(self):
        try:
            i2c = busio.I2C(board.SCL, board.SDA, frequency=4800, timeout=10000)
        except:
            try:
                i2c = busio.I2C(board.SCL, board.SDA, frequency=4800)
                """Blinka does not use keyword argument `timeout`"""
            except:                
                pass
                """perhaps i2c already initated from another test"""

        logger.info("i2ctest: trying to lock I2C bus with try_lock(): "+str(i2c.try_lock()))
        logger.info("i2ctest: scanning I2C bus with scan(), found devices:")
        try:
            addrs = i2c.scan()
            #[hex(x) for x in i2c.scan()]
            idpairs=""
            for  a in addrs:
                try:
                    idpairs+=str(hex(a))+": "+self.ids[a]+", "
                except:
                    idpairs+=str(hex(a))+": unidentified, "
                    
            logger.info("i2ctest: "+idpairs)
        except:
            logger.info("i2ctest: Failed to scan")
        logger.info("i2ctest: trying to deinit I2C bus with deinit()")
        i2c.deinit()
        return True

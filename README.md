# About

This folder contains CircuitPython scripts\* with simple low-level tests, mostly for Raspberry Pi SBC & MCU (Pico) hardware.

The helper `testsetup.py` should be saved to the /lib folder on the CIRCUITPY drive.


## Python on an SBC

```
ipython -i testname.py
In [1]: testname=testname()
        testname.test()
```

## CircuitPython on an MCU

1. Save `testname.py` to the `lib/` folder on the `CIRCUITPY` drive

2. Copy below into `code.py` or, type on the REPL:
```
from testname import testname
testname=testname()
testname.test()
```


\* CircuitPython scripts generated from Jupyter Notebooks and structured as a Python modules. Each notebook (avilable upon request) should be runnable from Jupyter kernels, e.g. a **Python 3** kernel on a Raspberry Pi or similar SBC with Adafruit Blinka installed, or a **CircuitPython** kernel running on a Raspberry Pi Pico or similar MCU; the tests have been written with the ability to run on both.

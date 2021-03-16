# About

This folder contains notebooks with simple low-level tests, mostly for Raspberry Pi SBC & MCU (Pico) hardware.

The helper testsetup.py should be available, which it is by default from notebooks, and on CircuitPython it should be placed in the /lib folder.

Each notebook should be runnable from Jupyter kernels, e.g. a **Python 3** kernel on a Raspberry Pi or similar SBC with Adafruit Blinka installed, or a **CircuitPython** kernel running on a Raspberry Pi Pico or similar MCU; the tests have been written with the ability to run on both.

Each notebook is structured as a Python module and, as such, can be run outside of the notebook, e.g. with *File > Download as > Python (.py)*, and then:

## Python on an SBC

```
ipython -i testname.py
In [1]: i2ctest=i2ctest()
i2ctest.test()
```

## CircuitPython on an MCU

1. save `testname.py` to the `lib/` folder on `CIRCUITPY` drive

2. copy below to `code.py` or, type on the REPL:
```
from testname import testname
testname.test()
```


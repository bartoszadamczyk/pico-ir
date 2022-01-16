# Pico IR

[![Lint](https://github.com/bartoszadamczyk/pico-ir/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/bartoszadamczyk/pico-ir/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/github/license/bartoszadamczyk/pico-ir)](https://github.com/bartoszadamczyk/pico-ir/blob/main/LICENSE)

Complete IR library for Raspberry Pico

## Warning

Remember to check your modules' voltage, you might need logic level converter to convert between 3v3 and 5v! 

## Example

```python
import utime
from machine import Pin
from pico_ir import read_code, send_code, validate_code, InvalidCodeException

pin_in = Pin(20, Pin.IN, Pin.PULL_UP)
pin_out = Pin(21, mode=Pin.OUT)

while True:
    out = read_code(pin_in)
    # ignore random signals 
    if out:
        try:
            validate_code(out)
            print(out)
            utime.sleep(3)
            send_code(pin_out, out)
        except InvalidCodeException:
            print("InvalidCodeException:" + out)
```

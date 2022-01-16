# Pico IR

Complete IR library for Raspberry Pi Pico

## Warning

Remember to check your modules' voltage, you might need logic level converter to convert between 3v3 and 5v! 

## Example

```python
import utime
from machine import Pin
from pico_ir import read_code, send_code, validate_code

pin_in = Pin(20, Pin.IN, Pin.PULL_UP)
pin_out = Pin(21, mode=Pin.OUT)

while True:
    out = read_code(pin_in)
    validate_code(out)
    utime.sleep(1)
    send_code(pin_out, out)
```

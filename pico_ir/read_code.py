import utime


def read_code(pin):
    raw = []

    # Signal is inverted:
    # 0 - high signal
    # 1 - low signal

    # wait for the leading pulse
    while pin.value() == 1:
        pass

    # 9ms leading pulse
    # 4.5ms space
    utime.sleep_us(13500)

    # Sample signal every 562.5µs
    # Time sensitive
    for i in range(1000):
        raw.append(pin.value())
        utime.sleep_us(56)

    code = ""
    count = 0

    for sample in raw:
        if sample == 1:
            # count low signal
            count += 1
        else:
            # ignore high signal
            if count > 0:
                # if low signal is longer than 562.5µs it 1 otherwise 0
                code += "1" if count > 10 else "0"
                count = 0

    # trim message transmission and repeat codes
    return code[0:32]

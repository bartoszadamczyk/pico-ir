from machine import PWM
import utime

HIGH_SIGNAL = int((2 ** 16) / 2)
LOW_SIGNAL = 0


def send_code(pin, code, freq=38000):
    pwm = PWM(pin)
    pwm.freq(freq)

    # 9ms leading pulse
    pwm.duty_u16(HIGH_SIGNAL)
    utime.sleep_us(9000)

    # 4.5ms space
    pwm.duty_u16(LOW_SIGNAL)
    utime.sleep_us(4500)

    # for 0 - 562.5µs pulse + 562.5µs space, total 1.125ms
    # for 1 – 562.5µs pulse + 1.6875ms space, total 2.25ms
    for bit in code:
        pwm.duty_u16(HIGH_SIGNAL)
        utime.sleep_us(562)
        pwm.duty_u16(LOW_SIGNAL)
        utime.sleep_us(1687 if bit == "1" else 562)

    # End of message transmission - final 562.5µs pulse
    pwm.duty_u16(HIGH_SIGNAL)
    utime.sleep_us(562)
    pwm.duty_u16(LOW_SIGNAL)
    utime.sleep_us(562)

    pwm.deinit()

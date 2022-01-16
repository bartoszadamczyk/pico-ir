class CodeInvalid(Exception):
    pass


class CodeTooShort(CodeInvalid):
    pass


class CodeTooLong(CodeInvalid):
    pass


def validate_code(code):
    if len(code) < 32:
        raise CodeTooShort

    if len(code) < 32:
        raise CodeTooLong

    # check 8-bit device address
    # following 8-bits should be a logical inverse of the device address
    for i in range(0, 8):
        if code[i] == code[i + 8]:
            raise CodeInvalid

    # check 8-bit command
    # following 8-bits should be a logical inverse of the command
    for i in range(16, 24):
        if code[i] == code[i + 8]:
            raise CodeInvalid
import random


def generate_ean13(prefix=[]):
    code = []

    # convert int or str of digits into list of digits
    if isinstance(prefix, (str, int)):
        prefix = list(str(prefix))

    # start new ean code with up to 12 digits from prefix
    if isinstance(prefix, list) and len(prefix) > 0:
        for digit in prefix:

            # if code = 12 digits, break
            if len(code) >= 12:
                break

            # if digit is int, append
            if isinstance(digit, int):
                code.append(digit)

            # if digit is str and is a digit, append as int
            elif isinstance(digit, str) and digit.isdigit():
                digit = code.append(int(digit))

    # add up to 12 random digits to complete code
    while len(code) < 12:
        code.append(random.randint(0, 9))

    # calculate checksum digit
    odd = code[0] + code[2] + code[4] + code[6] + code[8] + code[10]
    even = (code[1] + code[3] + code[5] + code[7] + code[9] + code[11]) * 3
    units = (odd + even) % 10
    check = 0
    if units != 0:
        check = 10 - units

    # add checksum digit
    code.append(check)

    # return as string of digits
    return ''.join([str(digit) for digit in code])


def main():
    pass


if __name__ == '__main__':
    main()

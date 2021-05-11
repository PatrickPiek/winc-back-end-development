import random


def generate_ean13(prefix=[]):
    code = []

    if isinstance(prefix, str):
        prefix = list(prefix)

    if isinstance(prefix, int):
        prefix = [int(i) for i in str(prefix)]

    # start new ean code with up to 12 digits from prefix
    if isinstance(prefix, list) and len(prefix) > 0:
        for digit in prefix:
            if len(code) >= 12:
                break
            if isinstance(digit, int):
                code.append(digit)
            elif isinstance(digit, str) and digit.isdigit():
                digit = code.append(int(digit))

    # add up to 12 random digits to complete
    while len(code) < 12:
        code.append(random.randint(0, 9))

    # calculate and add ‘check digit’
    # based on: https://www.open.edu/openlearn/science-maths-technology/exploring-communications-technology/content-section-2.1

    odd = code[0] + code[2] + code[4] + code[6] + code[8] + code[10]
    even = (code[1] + code[3] + code[5] + code[7] + code[9] + code[11]) * 3
    units = (odd + even) % 10
    check = 0
    if units != 0:
        check = 10 - units
    code.append(check)

    return ''.join([str(digit) for digit in code])


def main():
    pass


if __name__ == '__main__':
    main()

def format_currency(value=0):
    """Formats a float or int as a currency string with euro sign and a fractional of 2 digits"""
    return '€ {:,.2f} '.format(float(value))


def main():
    pass


if __name__ == '__main__':
    main()

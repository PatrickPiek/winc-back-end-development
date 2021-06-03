def parse_price(price):
    if price != None:
        try:
            return int(price)
        except ValueError:
            try:
                return float(price)
            except ValueError:
                raise ValueError('The ‘--price’ argument is not valid')
    return price


def main():
    pass


if __name__ == '__main__':
    main()

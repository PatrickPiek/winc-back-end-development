def get_bought_id(bought, sold, args):

    bought_id = None

    for b in bought.data:
        if b['product_name'] == args['product_name']:
            if sold.rowcount == 0:
                bought_id = b['id']
                break
            else:
                sold_state = False
                for s in sold.data:
                    if b['id'] == s['bought_id']:
                        sold_state = True
                if sold_state == False:
                    bought_id = b['id']
                    break

    return bought_id


def main():
    pass


if __name__ == '__main__':
    main()

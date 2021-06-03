def sort_list(data=[], column=''):
    if len(data) == 0:
        return []
    if len(data) == 1:
        return data
    return sorted(data, key=lambda key: key[column])


def main():
    pass


if __name__ == '__main__':
    main()

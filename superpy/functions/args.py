def check_required_arguments(args, required=()):
    for arg in required:
        if args[arg] == None:
            raise ValueError(f'The argument ‘{arg}’ is required')


def main():
    pass


if __name__ == '__main__':
    main()

def check_required_arguments(args, required=()):
    """Checks if all required arguments have a value other than None after parsing with argparse"""
    for arg in required:
        if args[arg] == None:
            raise ValueError(f'The argument ‘{arg}’ is required')


def main():
    pass


if __name__ == '__main__':
    main()

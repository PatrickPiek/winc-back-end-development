__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'

from Arguments import Arguments
from Router import Router


def main():

    arguments = Arguments()
    router = Router(arguments.vars)
    router.route()


if __name__ == '__main__':
    main()

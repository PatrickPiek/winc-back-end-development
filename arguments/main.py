# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# 1


def greet(name='stranger', template='Hello, <name>!'):
    return template.replace('<name>', name)

# 2


def force(mass=0, body='earth'):

    bodies = {
        'sun': 274,
        'mercury': 3.7,
        'venus': 9.8,
        'earth': 9.798,
        'moon': 1.62,
        'mars': 3.71,
        'jupiter': 24.92,
        'saturn': 10.44,
        'neptune': 11.15,
        'uranus': 8.87,
        'pluto': 9.8
    }

    return round(mass * bodies[body], 1)

# 3


def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    pull = G * ((m1 * m2) / (d ** 2))
    return pull


if __name__ == '__main__':

    # 1

    print(greet('Bob', 'What’s up, <name>!'))
    print(greet('Bob'))
    print(greet())

    # 2

    print(force(10, 'mercury'))
    print(force(0.123, 'proxima-centauri'))

    # 3

    print(pull(0.1, 5.972*10**24, 6371))

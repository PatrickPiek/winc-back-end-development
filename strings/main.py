# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scored = ['Ruud Gullit', 'Marco van Basten']
when = [32, 54]

scorers = scored[0] + ' ' + str(when[0]) + ', ' + scored[1] + ' ' + str(when[1])
print(scorers)

report = f'{scored[0]} scored in the {when[0]}nd minute\n{scored[1]} scored in the {when[1]}th minute'
print(report)

player = 'Ronald Koeman'
first_name = player[:player.find(' ')]
print(first_name)

last_name_len = len(player[-player.find(' '):])
print(last_name_len)

name_short = player[:player.find(' ')].upper()[:1] + '. ' + player[-player.find(' '):]
print(name_short)

chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')])).strip()
print(chant)

good_chant = chant
print(good_chant) # ;)
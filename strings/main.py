# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)
print(scorers)

report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'
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

good_chant = chant[-1:] != ' '
print(good_chant)
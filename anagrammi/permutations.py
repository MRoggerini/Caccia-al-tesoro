from itertools import permutations

word = 'idmelrapsi'
for i in permutations(word):
    print(''.join(i))


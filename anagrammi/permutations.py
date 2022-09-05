from itertools import permutations

word = 'tilao'
with open('parole.txt') as f:
    parole = f.readlines()

anagrammi = []

for i in parole:
    new = i.replace('\n', '')
    anagrammi.append(''.join(sorted(new)))

word = ''.join(sorted(word))

for i, parola in enumerate(anagrammi):
    if parola == word:
        print(parole[i])
        exit()

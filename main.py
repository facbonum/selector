import random

katas = [
    'Geki Sai-Dai Ichi',
    'Geki Sai-Dai Ni',
    'Saifa',
    'Seiyunchin',
    'Shisochin',
    'Kururunfa'
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(katas) # randomly choose a kata

print('What kata should I perform today?')
print(selected)
import random

symbols = [i for i in range(ord('a'), ord('z') + 1)] +\
    [i for i in range(ord('A'), ord('Z') + 1)] +\
    [i for i in range(ord('0'), ord('9') + 1)]

count = int(input('How much passwords do you need? '))
length = int(input('The length of the password? '))

with open('PassGen.txt', 'w') as f:
    for i in range(count):
        f.write("".join([chr(random.choice(symbols)) for j in range(length)]) + '\n')
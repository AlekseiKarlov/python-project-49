import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def noCorrect(a, b):
    print(f"'{a}' is wrong answer ;(. Correct answer was '{b}'.")


def arithmeticProgression():
    randa = randint(1, 99)
    randb = randint(1, 10)
    randc = randint(1, 10)
    c = randa
    i = 1
    otwet = ''
    while (i <= 10):
        otwet += ' '
        if (i == randc):
            d = c
            otwet += '..'
            c += randb
            i += 1
        else:
            otwet += str(c)
            c += randb
            i += 1
    print('Question:', otwet.strip())
    return d


def prostoe(d):
    n = 1
    count = 0
    while (n <= d):
        if (d % n == 0):
            count += 1
            n += 1
        else:
            n += 1
    if (count == 2):
        return 'yes'
    else:
        return 'no'
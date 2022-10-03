from random import randint
from .welcome import welcome, noCorrect
import prompt


def gcd_fun(x, y):
    if (y == 0):
        return x
    else:
        return gcd_fun(y, x % y)


def main():
    name = welcome()
    print('Find the greatest common divisor of given numbers.')
    n = 0
    while (n < 4):
        if (n == 3):
            print(f'Congratulations, {name}!')
            break
        randa = randint(0, 99)
        randb = randint(0, 99)
        print('Question:', randa, randb)
        otwet = gcd_fun(randa, randb)
        number = prompt.string('Your answer: ')

        if number.isnumeric() is False:
            print('Некорректный ввод')
            break

        if (otwet == int(number)):
            print('Correct!')
            n += 1
        else:
            noCorrect(number, otwet)
            break


if __name__ == '__main__':
    main()

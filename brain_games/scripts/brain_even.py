from random import randint
from brain_games.cli import welcome, noCorrect
import prompt


def main():
    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while (n < 4):
        if (n == 3):
            print(f'Congratulations, {name}!')
            break
        rand = randint(0, 99)
        print('Question:', rand)
        number = prompt.string('Your answer: ', rand)
        if (rand % 2 == 0 and number == "yes"):
            print('Correct!')
            n += 1
        elif (rand % 2 != 0 and number == "no"):
            n += 1
            print('Correct!')
        else:
            if (number == "yes"):
                noCorrect(number, 'no', name)
            elif (number == "no"):
                noCorrect(number, 'yes', name)
            else:
                print('Некорректный ввод')
            break


if __name__ == '__main__':
    main()

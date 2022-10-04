from random import randint
from brain_games.cli import welcome, prostoe, noCorrect
import prompt


def main():
    name = welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    n = 0
    while (n < 4):
        if (n == 3):
            print(f'Congratulations, {name}!')
            break
        randa = randint(1, 99)
        print('Question:', randa)
        otwet = prostoe(randa)
        number = prompt.string('Your answer: ')
        if (otwet == 'yes' and number == 'yes'):
            print('Correct!')
            n += 1
        elif (otwet == 'no' and number == 'no'):
            print('Correct!')
            n += 1
        else:
            noCorrect(number, otwet, name)
            break


if __name__ == '__main__':
    main()

from random import randint
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    n = 0
    znak = '+-*'
    while (n < 4):
        if (n == 3):
            print(f'Congratulations, {name}!')
            break
        pznak = random.choice(znak)
        randa = randint(0, 99)
        randb = randint(0, 99)
        print('Question:', randa, pznak, randb)
        number = prompt.string('Your answer: ')
        if number.isnumeric() == False:
            print('Некорректный ввод')
            break

        if (pznak == '+' and (randa + randb == int(number))):
            print('Correct!')
            n += 1
        elif (pznak == '-' and (randa - randb == int(number))):
            n += 1
            print('Correct!')
        elif (pznak == '*' and (randa * randb == int(number))):
            n += 1
            print('Correct!')
        else:
            if (pznak == "+"):
                print(f"'{number}' is wrong answer ;(. Correct answer was '{randa + randb}'.")
            elif (pznak == "-"):
                print(f"'{number}' is wrong answer ;(. Correct answer was '{randa - randb}'.")
            elif (pznak == "*"):
                print(f"'{number}' is wrong answer ;(. Correct answer was '{randa * randb}'.")
            else:
                print('Некорректный ввод')
            break



if __name__ == '__main__':
    main()
from .welcome import welcome, noCorrect, arithmeticProgression
import prompt


def main():
    name = welcome()
    print('What number is missing in the progression?')
    n = 0
    while (n < 4):
        if (n == 3):
            print(f'Congratulations, {name}!')
            break
        d = arithmeticProgression()
        number = prompt.string('Your answer: ')
        if number.isnumeric() is False:
            print('Некорректный ввод')
            break

        if (d == int(number)):
            print('Correct!')
            n += 1
        else:
            noCorrect(number, d)
            break


if __name__ == '__main__':
    main()

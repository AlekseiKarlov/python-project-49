import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def noCorrect(a, b):
    print(f"'{a}' is wrong answer ;(. Correct answer was '{b}'.")

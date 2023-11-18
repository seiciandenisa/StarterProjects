from random import randint

# Version 1

lower_number, higher_number = 1, 50
random_number: int = randint(lower_number, higher_number)
print(f' Guess the number from the range of {lower_number} to {higher_number}')

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number!')
        continue

    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('This is the number!')
        break


# Version 2

lower_num, higher_num = 1, 10
random_num: int = randint(lower_num, higher_num)
guesses = 3

print(f' Guess the number from the range of {lower_num} to {higher_num}')

while True:
    if guesses == 0:
        print(f'Game over, out of guesses!')
    elif guesses < 3:
        print(f'You have {guesses} left')
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number!')
        continue

    if user_guess > random_num:
        print('The number is lower')
        guesses -= 1
    elif user_guess < random_num:
        print('The number is higher')
        guesses -= 1
    else:
        print('This is the number!')
        break

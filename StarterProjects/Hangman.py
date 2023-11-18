from random import choice


def run_game():
    word: str = choice(['green', 'shake', 'truth'])

    username: str = input('What is your name? >>')
    print(f'Welcome {username}')

    # Setup
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blanks: int = 0  # blanks underscores where letters should be

        print('Word: ', end='')
        for character in word:
            if character in guessed:
                print(character, end='')
            else:
                print('_', end='')  # if a letter is not guessed, it puts an underscore
                blanks += 1  # when there are no blanks left, the user won the game

        print()  # Adds a blank line

        if blanks == 0:
            print('You guessed the word!')
            break

        guess: str = input('Enter a letter or the whole word: ').lower()

        if len(guess) == 1:  # Check if the user guessed one letter
            if guess in guessed:
                print(f'You already used: "{guess}". Please choose another letter!')
                continue
        guessed += guess
        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong. You have {tries} tries remaining')
        elif guess == word:  # Check if the user guessed the whole word
            print(f'Congratulations! You guessed the word!')
            break
        else:
            tries = 0
            print('No more tries remaining.. you lose.')
            break


if __name__ == '__main__':
    run_game()

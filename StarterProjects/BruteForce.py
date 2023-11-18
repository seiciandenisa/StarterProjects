import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open('words.text', 'r') as words:
        word_list: list[str] = words.read().splitlines()  # read every line and split into a list

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f'Common match: {match} (#{i})'  # position number of the match


def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):  # product will go through every single combination
        attempts += 1  # keeping track of the attempts
        guess: str = ''.join(guess)  # will return a list of combinations

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'

        print(guess, attempts)


def main():
    print('Searching..')
    password: str = 'abcd'

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):  # what common_guess will return, will assign it to common_match
        # but if common_match return None, the print will not execute
        print(common_match)
    else:
        for i in range(3, 6):
            if cracked := brute_force(password, length=4, digits=True, symbols=False):
                print(cracked)
            else:
                print("There is no match.")

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 's')


if __name__ == "__main__":
    main()

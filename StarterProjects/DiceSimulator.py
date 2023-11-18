import random


def roll_dice(amount: int = 2) -> list[int]:  # how many dices we want to roll
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []  # list to store the rolls
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input('How many dice would you like to roll?')

            if user_input.lower() == 'exit':
                print('Thank you for playing')
                break

            num_dice = int(user_input)
            rolls = roll_dice(int(user_input))

            total_sum = sum(rolls)

            print(*roll_dice(int(user_input)), sep=", ")
            print(f'You rolled  {rolls} rolls with a total of {total_sum}')
            # * is to unpack the list that we have and separate them using the sep
        except ValueError:
            print('(Please enter a valid number)')


if __name__ == '__main__':
    main()

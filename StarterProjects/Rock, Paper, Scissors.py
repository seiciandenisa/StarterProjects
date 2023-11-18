import random
import sys
import emoji


class RPS:
    def __init__(self):
        print('Welcome to Rock, Paper & Scissors!')

        self.moves: dict = {'rock': '', 'paper': 'Paper', 'scissors': 'Scissors'}
        self.valid_moves: list[str] = list(
            self.moves.keys())  # a list that containes the keys of the dictionary so that
        # the user can only select from this ones

    def play_game(self):
        user_move: str = input('Rock, paper or scissors? >> ').lower()

        if user_move == 'exit':
            print('Thank you for playing!')
            sys.exit()
        if user_move not in self.valid_moves:
            print('Invalid move..')
            return self.play_game()  # recursive loop

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print('-----')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('-----')

    def check_moves(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It is a tie!')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win')
        else:
            print('You lose!')


if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()

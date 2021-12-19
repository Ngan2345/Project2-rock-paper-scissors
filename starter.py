import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        answer = input("You play rock, paper or scissors?").lower()
        while answer not in moves:
            print("Invalid Input. Please try again!")
            answer = input("You play rock, paper or scissors?")
        return answer


class ReflectPlayer(RandomPlayer):

    def __init__(self):
        super().__init__()
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(RandomPlayer):

    def __init__(self):
        super().__init__()
        self.current = 0

    def move(self):
        my_move = None
        if self.current == 0:
            my_move = moves[0]
            self.current = self.current + 1
        elif self.current == 1:
            my_move = moves[1]
            self.current = self.current + 1
        else:
            my_move = moves[2]
            self.current = self.current + 1
        return my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            print("**PLAYER 1 WINS!**")
            self.p1.score += 1
        elif beats(move2, move1) is True:
            print("**PLAYER 2 WINS!**")
            self.p2.score += 1
        else:
            print("**TIE!**")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(
                  f"Score: Player 1: {self.p1.score},"
                  f"Player 2: {self.p2.score}")
        print("Game over!")
        if self.p1.score > self.p2.score:
            print("**PLAYER 1 WINS AFTER THREE ROUNDS!**")
        elif self.p1.score < self.p2.score:
            print("**PLAYER 2 WINS AFTER THREE ROUNDS!**")
        else:
            print("**IT IS A TIE AFTER THREE ROUNDS!**")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
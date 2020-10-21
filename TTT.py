
# coding: utf-8

# In[21]:


import games
from games import GameState
infinity = float('inf')


# In[31]:


class TicTacToe(games.Game):
    """Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""

    def __init__(self, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        self.initial = games.GameState(to_move='X', utility=0, board={}, moves=moves)
        self.show_moves = True

    def actions(self, state):
        """Legal moves are any square not yet taken."""
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board,
                         moves=moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if it is won or there are no empty squares."""
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        """Return true if there is a line through move on board for player."""
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k

    def play_game(self, *players):
        """Play an n-person, move-alternating game. This a version of
        the method from the aima-python games.py program that has been
        modified to optionaly print moves made by each player."""
        state = self.initial
        while True:
            for player_num, player in enumerate(players):
                player_num += 1
                print("  STATE:", state)
                move = player(self, state)
                state = self.result(state, move)
                if self.show_moves:
                    print("  Player{} moves {}".format(player_num, move))
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))



# In[32]:


a_game = TicTacToe()


# In[33]:


print(a_game)


# A player is represented by a search function that takes a game instance and a state and returns a move.   The game's methods (actions, result, utility and terminal_test) do the real work
# 
# The aima code defines several search functions and some players based on them

# In[34]:


# minimax returns a move by using the minimax algorithm
# to search all the way down to leaves to choose best move 
minimax = lambda g, s: games.minimax_decision(s, g)

# these return a move by using the alphabeta algorithm
# to search to a given depth to choose best move
dumb = lambda g, s: games.alphabeta_cutoff_search(s, g, d=1)
smart = lambda g, s: games.alphabeta_cutoff_search(s, g, d=3)
smarter = lambda g, s: games.alphabeta_cutoff_search(s, g, d=20)

# Smartest return a move by using the alphabeta algorithm
# to search down to leaves to choose best move
smartest = games.alphabeta_player

# random just returns a random move
random = games.random_player


# In[35]:


a_game = TicTacToe()
a_game.play_game(minimax, minimax)


# In[36]:


a_game = TicTacToe()
a_game.play_game(smart, smarter)


# In[38]:


a_game = TicTacToe()
a_game.play_game(smartest, smartest)


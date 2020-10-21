from collections import namedtuple
import games

infinity = float('inf')


class Nim(games.Game):

    """ Nim is a two player game where the players are identified as 1
    and 2.  Player 1 is first to move. The state of the game is a
    namedtuple with at least two attributes: to_move (the player whose
    turn it is to move) and board (a Python data structure
    representing how many heaps there are and how many objects are in
    each)."""

    def __init__(self, heaps=[1,1], show_moves=True):
        self.show_moves = show_moves
        self.heaps = heaps
        self.initial = games.GameState(to_move=1, board=heaps, utility=0, moves=[])

    def actions(self, state):
        """ Given a state, return a list of legal moves.  How you
        represent a move is up to you and will depend on how you
        represent the board"""
        moves = []
        for heap_num in range(len(state.board)):
            for remove in range(1,state.board[heap_num]+1):
                moves.append((heap_num, remove))
        #print('legal moves in %s are %s' % (state, moves))
        return moves

    def result(self, state,  move):
        """Given a move and a state, returns a representation of the
        new state that results after making the move."""
        #if not move: return state
        #print("Player",state.to_move,"making move",move,"in state",state)
        (heap_num, to_remove) = move
        h = state.board[:]
        h[heap_num] = h[heap_num] - to_remove
        nextPlayer = 1 if state.to_move == 2 else 2
        utility = self.utility(state, nextPlayer)
        new_state = games.GameState(to_move=nextPlayer, board=h, utility=utility, moves=[])
        #print("from", state, "move", move,"resultin in", new_state)
        return(new_state)

    def terminal_test(self, state):
        """ Returns True iff state is a terman state, i.e., one in
        which no moves are possible."""
        #print('Terminal test', state, "is", sum(state.board) == 0)
        return (sum(state.board) == 0)

    def utility(self, state, player):
        """ Given a state, returns a a number representing the state's
        utility w.r.t. player. This could be as simple as +infinity if
        it is a win for the player and -infinity if it is a win for
        the player's opponent and 0 if it is not a terminal state.  A
        better utility function would assign intermediate values for
        non-terminal states."""
        if sum(state.board) == 0:
            return infinity if player == state.to_move else -infinity
        else:
            return 0

        return 

    def __repr__(self):
        return "Nim({})".format(self.heaps)

    def play_game(self, *players):
        """Play an n-person, move-alternating game. This a version of
        the method from the aima-python games.py program that has been
        modified to optionaly print moves made by each player."""
        state = self.initial
        while True:
            for player_num, player in enumerate(players):
                player_num += 1
                move = player(self, state)
                state = self.result(state, move)
                if self.show_moves:
                    print("  Player{} moves {} => {}".format(player_num, move, state.board))
                if self.terminal_test(state):
                    self.display(state)
                    return self.utility(state, self.to_move(self.initial))



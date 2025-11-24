import search
import random

# Beginning of added by Linda
class ConnectFour(search.Problem):
    """ The problem of creating an intelligent bot to play connect four with.
    In a 7X6 grid, The goal is to get four of the same color of pieces horizonally, 
    vertically, or diagonally before opponent. Game is finished if either player is 
    able to do this or no pieces remain in a draw (and counter of n == 0) """
        
        

    """ A state is an array of pieces, E = Empty, R = Red, and Y = Yellow, 
    current player's turn: 0 for Bot, 1 for person, and number of pieces left to play.
    Counter starts at 42"""    

    def __init__(self, initial):
        """ Number of pieces left is listed first followed by grid then turn """
        super().__init__((initial[0], initial[1], initial[2]))

    

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
            An action is placing a piece on the grid """
        cntr = state[0]
        grid = state[1]
        turn = state[2]
        all_actions = []
            
      
        return all_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
            Action is the X, Y location of the ne piece """
        cntr = state[0]
        turn = state[2]
        
        grid = list(state[1])
        
        grid_lists = [list(t) for t in grid]
        """ Place piece and decrement counter """ 
        cntr = cntr - 1
        
        
       
        return (cntr,tuple(grid), turn)

    def goal_test(self, state):
        """ State is a goal when counter == 0 or a player has four pieces horizonally, vertically, or diagonally"""
        winner, color = ConnectFour.check_four_in_a_row(state[1])
        if winner: return 1
        return state[0] == 0
    
    
    def h(self, node):
        """Define some heuristic if using A* Search"""
        num = 1
        return num 
  
    def check_four_in_a_row(board):
        rows = len(board)
        cols = len(board[0])
        
        # Check horizontal
        for r in range(rows):
            for c in range(cols - 3):  # Only check up to the 4th to last column
                if board[r][c] != 'E' and \
                board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    if board[r][c] == 'Y':
                        return True, 'Y'
                    else: return True, 'R'

        # Check vertical
        for c in range(cols):
            for r in range(rows - 3):  # Only check up to the 4th to last row
                if board[r][c] != 'E' and \
                board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    if board[r][c] == 'Y':
                        return True, 'Y'
                    else: return True, 'R'

        # Check diagonal (top-left to bottom-right)
        for r in range(rows - 3):
            for c in range(cols - 3):
                if board[r][c] != 'E' and \
                board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    if board[r][c] == 'Y':
                        return True, 'Y'
                    else: return True, 'R'

        # Check diagonal (top-right to bottom-left)
        for r in range(rows - 3):
            for c in range(3, cols):  # Start from the 4th column
                if board[r][c] != 'E' and \
                board[r][c] == board[r+1][c-1] == board[r+2][c-2] == board[r+3][c-3]:
                    if board[r][c] == 'Y':
                        return True, 'Y'
                    else: return True, 'R'

        return False, 'E'
  
if __name__ == "__main__":
    board = tuple(tuple('E' for _ in range(6)) for _ in range(7))
    fo1 = ConnectFour((42, board, 0))

    print(search.astar_search(fo1).path())
    print(search.astar_search(fo1).solution())


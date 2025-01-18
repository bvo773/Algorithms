"""
TIC-TAC-TOE is played by two players A and B on a 3 x 3 grid. The rules of TIC-TAC-TOE are:
  - Players take turns placing characters into empty squares ' '.
  - The first player A always places 'x' characters, while the second player B always places 'o' characters.
  - 'X' and 'O' characters are always placed into empty squares, never on filled ones.
  - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
  - The game also ends if all squares are non-empty.
  - No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [row-i, col-i] indicates that the i^th move will be played on grid[row-i][col-i], return the winner
of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e. it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first
Input: moves = [ [0,0], [2,0] ,[1,1], [2,1], [2,2] ] 
Output: "A"
Explanation: A wins, they always play first. 

WINNING CONDITION
ROW       COLUMN    DIAGONAL     ANTIDIAGONAL
0 0 0     0         0                 0
          0           0             0
          0             0         0  

row=0     col=0     col=row       col+row = 2
"""

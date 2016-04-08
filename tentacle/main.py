import matplotlib
matplotlib.use('Qt4Agg')

from tentacle.board import Board
from tentacle.game import Game
from tentacle.strategy import StrategyTD

def sim1():
    Board.BOARD_SIZE = 9
    board = Board()
     
    s1 = StrategyTD(83, 41)
    
    s1.alpha = 0.1
    s1.beta = 0.1
     
    win1 = 0
    win2 = 0
    draw = 0
    for i in range(1):
        g = Game(board, s1, s1)
        g.step_to_end()
        win1 += 1 if g.winner() == 1 else 0
        win2 += 1 if g.winner() == 2 else 0
        draw += 1 if g.winner() == 0 else 0
         
        
    

if __name__ == '__main__': 
#     board = Board(9)
#     board.move(3, 3, 2)
#     board.move(3, 2, 1)
#     board.show()
    sim1()
    
#Connect 4

import numpy as np
import pygame
import sys
import math

ROWS = 6
COLUMNS = 7

#colours
WHITE = (255,255,255)
BLUE = (0,0,190)
YELLOW = (255,255,0)
RED = (220,22,0)
BLACK = (0,0,0)
ORANGE = (255,140,0)

def make_board():
    #create a matrix of 0 (6 rows, 7 columns)   
    board = np.zeros((6,7))
    np.flipud(board)
    return board
        
def insert_coin(board, row, column, coin):
    #coin insertion
    board[row][column]=coin

def overflow_check(board, column):
    #checks if fifth row is still free or occupied, fifth row is the top row
    return board[5][column]==0

def open_row_check(board, column):
    #checks for the next open row or "0"
    for r in range(ROWS):
        if board[r][column]==0:
            return r
def flip_board(board):
    #since numpy matrix starts (0,0) at top left
    print(np.flip(board, 0))

def winning_coin(board, coin):
    #horizontal check, only 3 of the columns can work
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == coin and board[r][c+1] == coin and board[r][c+2] == coin and board [r][c+3] == coin:
                return 1==1
    #vertical check, can only be in bottom 3 rows
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if board[r][c] == coin and board[r+1][c] == coin and board[r+2][c] == coin and board [r+3][c] == coin:
                return 1==1    
    #diagonal positive slopes check (/) last point is (3,4)
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if board[r][c] == coin and board[r+1][c+1] == coin and board[r+2][c+2] == coin and board [r+3][c+3] == coin:
                return 1==1
    #diagonal negative slopes check (/) starts at 4th row (3)
    for c in range(COLUMNS-3):
        for r in range(3,ROWS):
            if board[r][c] == coin and board[r-1][c+1] == coin and board[r-2][c+2] == coin and board[r-3][c+3] == coin:
                return 1==1
def draw_board(board):
    #sets background as white
    screen.fill(WHITE)
    for c in range(COLUMNS):    
        for r in range(ROWS):
            #creates a blue rectangle for board outline
            pygame.draw.rect(screen, BLUE,(c*SQSIZE,r*SQSIZE+SQSIZE,SQSIZE,SQSIZE))
            #creates a circle for each column x row
            pygame.draw.circle(screen, WHITE,(int(c*SQSIZE+50),int(r*SQSIZE+150)),int(SQSIZE/2-6))

    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                #player 1 colour (RED)
                pygame.draw.circle(screen, RED,(int(c*SQSIZE+50),height-int(r*SQSIZE+150-SQSIZE)),int(SQSIZE/2-6))
            elif board[r][c] == 2:
                #player 2 colour (YELLOW)
                pygame.draw.circle(screen, YELLOW,(int(c*SQSIZE+50),height-int(r*SQSIZE+150-SQSIZE)),int(SQSIZE/2-6))
        pygame.display.update()
                
board = make_board()    
print(board)
#sets gameover as False
game_over = False

#allows alternation of turns
turn = 0

#initializes pygame
pygame.init()

#size of one square
SQSIZE = 100

#number of columns times sqsize
width = COLUMNS * SQSIZE

#number of rows times sqsize, plus one for the extra top row (for selection)
height = (ROWS+1) * SQSIZE

#into a tuple
size = (width, height)

screen = pygame.display.set_mode(size)
#draws board (blue rectangle and white circles)
draw_board(board)
pygame.display.update()
#sets the font
font = pygame.font.SysFont("arial", 65)

#runs the game as long as gameover = false
while not game_over:

    for event in pygame.event.get():
        #so that pygame doesnt crash when you click top right 'x'
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        #during mouse motion, this will show the coin moving around. Color of coin depends on turn
        if event.type == pygame.MOUSEMOTION:
            #creates a white board at the top so that it the coin doesn't continue to appear
            pygame.draw.rect(screen,WHITE,(0,0, width, SQSIZE))
            posx = event.pos[0]
            #red colour for red coin
            if turn == 0:
                pygame.draw.circle(screen,RED,(posx,int(SQSIZE/2)), int(SQSIZE/2-6))
            #yellow colour for yellow coin
            else:
                pygame.draw.circle(screen,YELLOW,(posx,int(SQSIZE/2)), int(SQSIZE/2-6))
        pygame.display.update()
        #during click
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('')
            #ask for player 1 input
            if turn == 0:
                posx = event.pos[0]
                column = int(math.floor(posx/SQSIZE))
                #checks if top row is full
                if overflow_check(board,column):
                    row = open_row_check(board, column)
                    insert_coin(board, row, column, 1)
                    #if win is true, when turn is for player 1 prints player 1 wins
                    if winning_coin(board, 1):
                        msg = font.render('Winning Coin Player 1 Wins',0,BLACK)
                        #updates top of the screen to display the message
                        screen.blit(msg, (15,10))
                        pygame.display.update()
                        #need to insert a range so that game doesn't immeiately close and message disspears
                        for loop in range(21000000):
                            if loop == 10:
                                game_over = True
        
            #ask for player 2 input
            else:
                posx = event.pos[0]
                column = int(math.floor(posx/SQSIZE))
                #checks if top row is full
                if overflow_check(board, column):
                    row = open_row_check(board, column)
                    insert_coin(board, row, column, 2)
                    # if win is true, when turn is for player 2 prints player 2 wins
                    if winning_coin(board, 2):
                        msg = font.render('Winning Coin Player 2 Wins',0,BLACK)
                        #updates top of the screen to display the message
                        screen.blit(msg, (15,10))
                        pygame.display.update()
                        #need to insert a range so that game doesn't immeiately close and message disspears
                        for loop in range(21000000):
                            if loop == 10:
                                game_over = True  

            draw_board(board)
    #alternates between turns
            turn+=1
            turn = turn%2
                
    
        
    
'''
References

1. Got help from SciPy.org explaining how to flip an array on NumPy. https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.flip.html

2. Got help from pygame explaining draw functions and screen display. http://pygame.org/docs/ref/draw.html

3. Understanding Event Pygame. https://www.pygame.org/docs/ref/event.html

4. Understand pygame mouse movement and clicking. https://www.pygame.org/docs/ref/event.html

5. Understanding MOUSEBUTTON DOWN https://www.pygame.org/docs/ref/event.html

6. Returning the floor of x as a float, the largest ingeter value less than or equal to x. https://docs.python.org/2/library/math.html

7. Pygame MOUSEMOTION (posx). https://www.pygame.org/docs/ref/event.html
'''

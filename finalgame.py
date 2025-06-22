#finalproject

import pygame
import random
 

#initiallize font 
pygame.font.init()
 
#board Dimensions
width = 800
height = 700
board_width = 300  
board_height = 600  
block_size = 30
 
top_x = (width - board_width) // 2
top_y = height - board_height
 

#music & sounds
pygame.mixer.init()
music = pygame.mixer.music.load("tetristheme.mp3")
pygame.mixer.music.set_volume(0.2)
lineclear=pygame.mixer.Sound("lineclear.wav")
lineclear.set_volume(0.05)
gameoversound=pygame.mixer.Sound("gameover.wav")
gameoversound.set_volume(1)


#pieces in array format

S_piece = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z_piece = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I_piece = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O_piece = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J_piece = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L_piece = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T_piece = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]
#put pieces in list, matched w/ its colours
tetrominoes = [S_piece, Z_piece, I_piece, O_piece, L_piece, J_piece, T_piece]

colours = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (250, 242, 10), (252, 171, 30), (50, 63, 209), (196, 62, 237)]

#fonts,dimensions,images for menu
myFont=pygame.font.Font("tetrisfont.ttf",60)
text1=myFont.render("Start", True,(255,255,255))
text2=myFont.render("Exit",True,(255,255,255))
text3=myFont.render("Controls",True,(255,255,255))
mouseX=0
mouseY=0
buttonX=300
buttonW=200
buttonY=50
buttonH=100
buttonX2=310
buttonW2=200
buttonY2=220
buttonH2=100
buttonX3=250
buttonW3=500
buttonY3=400
buttonH3=100
backX=0
backY=600
backW=100
backH=84
menubg=pygame.image.load('tetrismenu.png')
controlsimage=pygame.image.load('tetriscontrols.jpeg')
back=pygame.image.load('backarrow.png')

#shows user game controls
def controls():
    run= True
    while run:
        
        gameWindow.fill((255,255,255))
        gameWindow.blit(controlsimage,(25,200))
        pygame.draw.rect(gameWindow,(255,255,255),(0,625,100,84))
        gameWindow.blit(back,(0,625))
        pygame.display.update()
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                mouseX,mouseY=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if(mouseX>backX and mouseX<backX+backW and mouseY>backY and mouseY<backY+backH):
                       menu(mouseX,mouseY,buttonX,buttonY,buttonH)
                   
def menu(mouseX,mouseY,buttonX,buttonY,buttonH):
    run = True
    while run:
        #draw layout of menu
        gameWindow.fill((0,0,0))
        gameWindow.blit(menubg,(0,145))

        pygame.draw.rect(gameWindow,(0,0,0),(buttonX,buttonY,buttonW,buttonH))
        gameWindow.blit(text1,(buttonX-2,buttonY+50))
        pygame.draw.rect(gameWindow,(0,0,0),(buttonX,buttonY+80,buttonW+5,buttonH-25))

        pygame.draw.rect(gameWindow,(0,0,0),(buttonX2,buttonY2,buttonW2,buttonH2))
        gameWindow.blit(text2,(buttonX2-2,buttonY2+50))
        pygame.draw.rect(gameWindow,(0,0,0),(buttonX2,buttonY2+80,buttonW2+5,buttonH2-25))

        pygame.draw.rect(gameWindow,(0,0,0),(buttonX3,buttonY3,buttonW3,buttonH3))
        gameWindow.blit(text3,(buttonX3-2,buttonY3+50))
        pygame.draw.rect(gameWindow,(0,0,0),(buttonX3,buttonY3+80,buttonW3+150,buttonH-25))

        pygame.display.update()
        pygame.time.delay(5)
        #mouse cooordinates+detecting when it clicks button
        for event in pygame.event.get():
            if event.type==pygame.MOUSEMOTION:
                mouseX,mouseY=pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if(mouseX>buttonX and mouseX<buttonX+buttonW and mouseY>buttonY and mouseY<buttonY+buttonH):
                        main()
                    if(mouseX>buttonX2 and mouseX<buttonX2+buttonW2 and mouseY>buttonY2 and mouseY<buttonY2+buttonH2):
                        pygame.quit()
                    if(mouseX>buttonX3 and mouseX<buttonX3+buttonW3 and mouseY>buttonY3 and mouseY<buttonY3+buttonH3):
                        controls()
                        
#draw window
gameWindow = pygame.display.set_mode((width, height)) 
 
class Piece(object):
    rows = 20  
    columns = 10  
 
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = colours[tetrominoes.index(shape)]
        self.rotation = 0

       
def make_grid(locked_positions={}):
    board = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                board[i][j] = c
    return board
 
 
def shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions
 
#check if space shape is in is available  
def available_space(shape, board):
    open_positions = [[(j, i) for j in range(10) if board[i][j] == (0,0,0)] for i in range(20)]
    open_positions = [j for sub in open_positions for j in sub]
    formatted = shape_format(shape)
 
    for pos in formatted:
        if pos not in open_positions:
            if pos[1] > -1:
                return False
 
    return True
 
 
def gameover(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 
#get a random shape 
def get_shape():
    global tetrominoes, colours
 
    return Piece(5, 0, random.choice(tetrominoes))
 
 
def draw_text_middle(text, size, color, gameWindow2):
    font = pygame.font.SysFont('arial', size, bold=True)
    label = font.render(text, 1, color)
 
    gameWindow2.blit(label, (top_x + board_width/2 - (label.get_width() / 2), top_y + board_height/2 - label.get_height()/2))
 
#draw grid 
def draw_grid(gameWindow2, row, col):
    sx = top_x
    sy = top_y
    for i in range(row):
        pygame.draw.line(gameWindow2, (128,128,128), (sx, sy+ i*30), (sx + board_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(gameWindow2, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + board_height))  # vertical lines


#burning lines
def burn_lines(board, locked):
   
     
     inc = 0
     
     for i in range(len(board)-1,-1,-1):
        row = board[i]
        if (0, 0, 0) not in row:
            inc += 1
            
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
     if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
                lineclear.play()
 #draw next shape
def next_shape(shape, gameWindow2):
    font = pygame.font.SysFont('arial', 30)
    label = font.render('Next Piece', 1, (255,255,255))
 
    sx = top_x + board_width + 50
    sy = top_y + board_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(gameWindow2, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
 
    gameWindow2.blit(label, (sx + 10, sy- 30))
 
#game window + layout of game window
def draw_window(gameWindow2):
    gameWindow2.fill((0,0,0))
    
    title= pygame.image.load('tetristitle.png')
    gameWindow2.blit(title,(250,-65))
    for i in range(len(board)):
        for j in range(len(board[i])):
            pygame.draw.rect(gameWindow, board[i][j], (top_x + j* 30, top_y + i * 30, 30, 30), 0)
 
    # draw game board and border around it
    draw_grid(gameWindow, 20, 10)
    pygame.draw.rect(gameWindow2, (255, 255, 255), (top_x, top_y, board_width, board_height), 5)
    
 
 
def main():
    pygame.mixer.music.play(-1)
    global board
    
    locked_positions = {}  
    board = make_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
 
    while run:
        gravity = 0.3
 
        board = make_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
 
        #make pieces fall constantly
        if fall_time/1000 >= gravity:
            fall_time = 0
            current_piece.y += 1
            if not (available_space(current_piece, board)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        #user controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
     
            if event.type == pygame.KEYDOWN:
                #move piece left
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not available_space(current_piece, board):
                        current_piece.x += 1
                #move piece right
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not available_space(current_piece, board):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not available_space(current_piece, board):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # soft drop
                    current_piece.y += 1
                    if not available_space(current_piece, board):
                        current_piece.y -= 1
                     #hard drop
                if event.key == pygame.K_SPACE:
                   while available_space(current_piece, board):
                       current_piece.y += 1
                   current_piece.y -= 1
                   print(shape_format(current_piece))  
                
 
        shape_pos = shape_format(current_piece)
 
        
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                board[y][x] = current_piece.color
 
        # when pieces lands
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
 
            # check rows after a piece lands
            burn_lines(board, locked_positions)
 
        draw_window(gameWindow)
        next_shape(next_piece, gameWindow)
        pygame.display.update()
 
        
        if gameover(locked_positions):
            
            run = False

    
    #if pieces top out
    pygame.mixer.music.stop()
    draw_text_middle("GAME OVER", 100, (255,255,255), gameWindow)
    gameoversound.play()
    pygame.display.update()
    pygame.time.delay(2000)
    
#####

#when code is run 
menu(mouseX,mouseY,buttonX,buttonY,buttonH) 

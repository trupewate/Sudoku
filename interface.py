

import sys
import pygame as pg
from constants import ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, WHITE, BLACK, YELLOW, BLUE, FONT_SIZE, MARGIN, OFFSET
import sudoku

pg.init()
screen_size = WIDTH, HEIGHT
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Sudoku")
font = pg.font.SysFont(None, FONT_SIZE)


#initialising sudoku
sudoku = sudoku.Sudoku()
number_grid = sudoku.grid



def draw_background():
    screen.fill(pg.Color(WHITE))
    pg.draw.rect(screen, BLACK, pg.Rect(MARGIN, MARGIN, WIDTH - MARGIN * 2, HEIGHT - MARGIN * 2), 10)
    i = 1
    while (i * SQUARE_SIZE) < WIDTH - MARGIN * 2:
        line_width = 5 if i % 3 > 0 else 10
        pg.draw.line(screen, pg.Color(BLACK), pg.Vector2((i * SQUARE_SIZE) + MARGIN, MARGIN), pg.Vector2((i * SQUARE_SIZE) + MARGIN, 730), line_width)
        pg.draw.line(screen, pg.Color(BLACK), pg.Vector2(MARGIN, (i * SQUARE_SIZE) + MARGIN), pg.Vector2(730, (i * SQUARE_SIZE) + MARGIN), line_width)
        i += 1

def draw_numbers():
    row = 0
    while row < 9:
        col = 0
        while col< 9:
            output = number_grid[row][col]
            if output != '0':
                if sudoku.originalgrid[row][col] == '0':
                    n_text = font.render(str(output), True, BLUE)
                else:
                    n_text = font.render(str(output), True, BLACK)
                
                screen.blit(n_text, pg.Vector2((col * SQUARE_SIZE) + OFFSET + 4, (row * SQUARE_SIZE)+ OFFSET - 2))
            col+=1
        row +=1

def highlight(selected):
    if selected != None:
        row, col = selected
        pg.draw.rect(screen, YELLOW, (col * SQUARE_SIZE + MARGIN + 2, row * SQUARE_SIZE + MARGIN + 2, SQUARE_SIZE - 2, SQUARE_SIZE - 2))
    
def calc_row_col(x, y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
    
def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            row, col = calc_row_col(x, y)
            sudoku.select(row, col)
        elif event.type == pg.KEYDOWN:
            if sudoku.selected != None:
                row, col = sudoku.selected
                if event.key == pg.K_1:
                    sudoku.grid[row][col] = '1'
                    sudoku.selected = None
                if event.key == pg.K_2:
                    sudoku.grid[row][col] = '2'
                    sudoku.selected = None
                if event.key == pg.K_3:
                    sudoku.grid[row][col] = '3'
                    sudoku.selected = None
                if event.key == pg.K_4:
                    sudoku.grid[row][col] = '4'
                    sudoku.selected = None
                if event.key == pg.K_5:
                    sudoku.grid[row][col] = '5'
                    sudoku.selected = None
                if event.key == pg.K_6:
                    sudoku.grid[row][col] = '6'
                    sudoku.selected = None
                if event.key == pg.K_7:
                    sudoku.grid[row][col] = '7'
                    sudoku.selected = None
                if event.key == pg.K_8:
                    sudoku.grid[row][col] = '8'
                    sudoku.selected = None
                if event.key == pg.K_9:
                    sudoku.grid[row][col] = '9'
                    sudoku.selected = None
                if event.key == pg.K_BACKSPACE:
                    sudoku.grid[row][col] = '0'
                    sudoku.selected = None

            
    draw_background()
    highlight(sudoku.selected)
    draw_numbers()
    pg.display.flip()

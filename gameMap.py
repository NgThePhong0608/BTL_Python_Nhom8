import pygame as pg
from init import *

game_map = []
for i in range(0, CELLS_ON_ROW * CELLS_ON_COL):
    game_map.append(0)
clock = pg.time.Clock()
move_down = CELLS_ON_ROW

# DRAW SCORE SECTION
game_point = 0


# TETROMINO DEFINES
oTetromino = [
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
]
zTetromino = [
    [0, 1, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [2, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [0, 1, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [2, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2]
]
rv_zTetromino = [
    [1, 2, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [1, 2, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2]
]
tTetromino = [
    [1, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [1, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [1, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2]
]
iTetromino = [
    [1, CELLS_ON_ROW + 1, CELLS_ON_ROW*2 + 1, CELLS_ON_ROW*3 + 1],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 3 + CELLS_ON_ROW],
    [1, CELLS_ON_ROW + 1, CELLS_ON_ROW*2 + 1, CELLS_ON_ROW*3 + 1],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 3 + CELLS_ON_ROW]
]
lTetromino = [
    [0, 1, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [2, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [1, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2, 2 + CELLS_ON_ROW*2],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, CELLS_ON_ROW*2]
]
rv_lTetromino = [
    [1, 2, CELLS_ON_ROW + 1, CELLS_ON_ROW*2 + 1],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 2 + CELLS_ON_ROW*2],
    [1, 1 + CELLS_ON_ROW, CELLS_ON_ROW*2, 1 + CELLS_ON_ROW*2],
    [0, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW]
]
tetrominos = [
    oTetromino,
    zTetromino,
    rv_zTetromino,
    tTetromino,
    iTetromino,
    lTetromino,
    rv_lTetromino
]
rotation = 0
rand_num = random.randint(0, 6)
rand_num_next = random.randint(0, 6)
tetromino = tetrominos[rand_num]
color = COLORS[rand_num]
color_next = COLORS[rand_num_next]
# DRAW STUFFS ON SCREEN
levelX = 660
levelY = NEXTTET_UPPER_GAP + 105

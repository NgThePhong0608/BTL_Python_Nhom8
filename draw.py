from gameMap import *


def drawLevel(lev):
    global level
    levelText = levelFont.render(
        "LV:" + "{:03d}".format(lev), True, (248, 255, 13))
    screen.blit(levelText, (levelX, levelY))
    pg.draw.rect(screen, WHITE, (520, 460, 260, 80), 2)
    screen.blit(evaImg, (522, 462))
    screen.blit(resetImg, (720, 640))
    screen.blit(exitImg, (520, 560))


def drawTetrisSurface():
    pg.draw.line(screen, WHITE, (500, 0), (500, SCREEN_HEIGHT), 2)
    pg.draw.rect(screen, (249, 44, 228), (LEFT_GAP-4, UPPER_GAP -
                 4, GRID_WIDTH + 8, GRID_HEIGHT + 8), 4)
    pg.draw.rect(screen, (40, 33, 33), (LEFT_GAP,
                 UPPER_GAP, GRID_WIDTH, GRID_HEIGHT))


def drawCell(pos, color):
    pg.draw.rect(screen, color,
                 (LEFT_GAP + ((pos + CELLS_ON_ROW) % CELLS_ON_ROW) * CELL_SIZE, UPPER_GAP + (pos // CELLS_ON_ROW) * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def drawTetromino(pos, color):
    for i in tetromino[rotation]:
        drawCell(pos + i, color)


def drawTakenTetrominos():
    for i in range(0, CELLS_ON_COL * CELLS_ON_ROW):
        if game_map[i] != 0:
            drawCell(i, game_map[i])


def showScore(point):
    pg.draw.rect(screen, (0, 255, 0), (textX, textY, 260, 160), 4)
    scoreText = nextTetFont.render("SCORE----", True, (0, 255, 0))
    screen.blit(scoreText, (textX + 18, textY + 16))
    scoreValue = nextTetFont.render(
        "----" + "{:05d}".format(point), True, (0, 255, 0))
    screen.blit(scoreValue, (textX, textY + 100))


def drawNextTetSection():
    next = nextTetFont.render("NEXT", True, (71, 244, 255))
    screen.blit(next, (NEXTTET_LEFT_GAP - 5, NEXTTET_UPPER_GAP - 70))
    pg.draw.rect(screen, (71, 244, 255), (NEXTTET_LEFT_GAP - 10,
                 NEXTTET_UPPER_GAP - 20, NEXTTET_WIDTH + 20, NEXTTET_HEIGHT + 40), 2)
    for i in tetrominos[rand_num_next][0]:
        pg.draw.rect(screen, color_next,
                     (NEXTTET_LEFT_GAP + ((i + CELLS_ON_ROW) % CELLS_ON_ROW) * CELL_SIZE, NEXTTET_UPPER_GAP + (i // CELLS_ON_ROW) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

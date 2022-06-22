from init import *
from draw import *
from checkEvent import *
from button import *

screen_looping = True
game_pause = False
current_speed = 0.27
fall_speed = current_speed
fall_time = 0
while screen_looping:
    pg.display.flip()
    # check game events from keyboard and outter stuffs
    if pg.key.get_pressed()[pg.K_DOWN]:
        if game_pause == False:
            fall_speed = 0.05
    for event in pg.event.get():
        timeBtn.click(event)
        exitBtn.click(event)
        resetBtn.click(event)
        if event.type == pg.QUIT:
            screen_looping = False
        if event.type == pg.KEYDOWN:
            if game_pause == False:
                if event.key == pg.K_LEFT:
                    if leftEdge(drop_pos):
                        drop_pos -= 1
                        move_down = 0
                if event.key == pg.K_RIGHT:
                    if rightEdge(drop_pos):
                        drop_pos += 1
                        move_down = 0
                if event.key == pg.K_SPACE:
                    if checkEdge(drop_pos) == False:
                        drop_pos = checkRot(drop_pos)
                        rotation = (rotation + 1) % 4
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                move_down = CELLS_ON_ROW
            if event.key == pg.K_RIGHT:
                move_down = CELLS_ON_ROW
            if event.key == pg.K_DOWN:
                fall_speed = current_speed
    screen.fill(BLACK)
    drawTetrisSurface()
    drawTakenTetrominos()
    drawNextTetSection()

    drawTetromino(drop_pos, color)
    timeBtn.draw()
    exitBtn.draw()
    resetBtn.draw()
    if checkLose(drop_pos):
        game_pause = True

    fall_time += clock.get_rawtime()
    clock.tick()
    if fall_time/1000 >= fall_speed:
        fall_time = 0
        if checkEdge(drop_pos) == False:

            drop_pos += move_down
        else:
            for i in tetromino[rotation]:
                game_map[drop_pos + i] = color
            checkFullAllRow(drop_pos)
            rand_num = rand_num_next
            tetromino = tetrominos[rand_num]
            color = color_next
            drop_pos = 5
            rotation = 0
            rand_num_next = random.randint(0, 6)
            color_next = COLORS[rand_num_next]
    if game_pause == True:
        clock.tick(0)
    showScore(game_point)
    drawLevel(level)

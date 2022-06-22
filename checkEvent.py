from gameMap import *


def checkLevel(point):
    global level
    global current_speed
    if point > 100:
        level = 5
        current_speed = 0.05
        return
    if point >= 80:
        level = 4
        current_speed = 0.1
        return
    if point >= 40:
        level = 3
        current_speed = 0.17
        return
    if point >= 20:
        level = 2
        current_speed = 0.2
        return


def checkTetLeft(tet):
    res = tet[0]
    for i in tet:
        if (i + CELLS_ON_ROW) % CELLS_ON_ROW < (res + CELLS_ON_ROW) % CELLS_ON_ROW:
            res = i
    return res


def checkTetRight(tet):
    res = tet[0]
    for i in tet:
        if (i + CELLS_ON_ROW) % CELLS_ON_ROW > (res + CELLS_ON_ROW) % CELLS_ON_ROW:
            res = i
    return res


def checkBottomCollision(pos):
    for i in tetromino[rotation]:
        if game_map[pos + i + CELLS_ON_ROW] != 0:
            return True
    return False


def checkEdge(pos):
    if (pos + tetromino[rotation][3]) in range(252, 264):
        return True
    if checkBottomCollision(pos):
        return True
    return False


def leftEdge(pos):
    for i in tetromino[rotation]:
        if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == 0:
            return False
        if game_map[pos + i - 1] != 0:
            return False
    return True


def rightEdge(pos):
    for i in tetromino[rotation]:
        if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == CELLS_ON_ROW - 1:
            return False
        if game_map[pos + i + 1] != 0:
            return False

    return True


def checkFullOneRow(pos):
    for i in range(pos, pos + 12):
        if game_map[i] == 0:
            return False
    return True


def checkFullAllRow(pos):
    global game_point
    global level
    first_row = (pos + tetromino[rotation][0]) // CELLS_ON_ROW
    second_row = (pos + tetromino[rotation][3]) // CELLS_ON_ROW
    col_take = []
    for i in range(first_row * CELLS_ON_ROW, second_row * CELLS_ON_ROW + CELLS_ON_ROW, CELLS_ON_ROW):
        if checkFullOneRow(i):
            col_take.append(i)
            for j in range(i, i + 12):
                game_map[j] = 0

    ct_length = len(col_take)
    if ct_length != 0:
        # GOT POINTS AFTER FULL ROW
        game_point = game_point + 10 * ct_length
        checkLevel(game_point)
        head_pos = col_take[0]
        for i in reversed(range(0, head_pos)):
            if game_map[i] != 0:
                res = game_map[i]
                game_map[i] = 0
                game_map[i + ct_length * CELLS_ON_ROW] = res


def checkRot(pos):
    new_rotation = (rotation + 1) % 4
    first_cell = checkTetLeft(tetromino[new_rotation])
    last_cell = checkTetRight(tetromino[new_rotation])
    length = (last_cell + CELLS_ON_ROW) % CELLS_ON_ROW - \
        (first_cell + CELLS_ON_ROW) % CELLS_ON_ROW
    if (pos + checkTetLeft(tetromino[rotation]) + CELLS_ON_ROW) % CELLS_ON_ROW < 5:
        for i in tetromino[new_rotation]:
            if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == 11:
                return ((pos // CELLS_ON_ROW) * CELLS_ON_ROW +
                        ((first_cell + pos) % CELLS_ON_ROW - (pos) % CELLS_ON_ROW))
    else:
        for i in tetromino[new_rotation]:
            if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == 0:
                return (pos // CELLS_ON_ROW) * CELLS_ON_ROW + 11 - length
    return pos


def checkLose(pos):
    for i in range(0, 12):
        if game_map[i] != 0:
            return True
    return False

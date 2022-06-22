import pygame as pg
from init import *
# BUTTON DEFINES
playImg = pg.image.load("./asset/play-64.png")
pauseImg = pg.image.load("./asset/pause-64.png")


class TimeButton:
    def __init__(self,  width, height, pos, img1, img2, color):
        # global font
        self.top_rect = pg.Rect(pos, (width, height))
        self.top_color = color
        self.play_img = img1
        self.pause_img = img2
        self.icon = img2
        self.text_rect = self.play_img.get_rect(center=self.top_rect.center)

    def draw(self):
        pg.draw.rect(screen, self.top_color, self.top_rect, border_radius=4)
        screen.blit(self.icon, self.text_rect)

    def click(self, event):
        global game_pause
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    game_pause = abs(game_pause - 1)
                    if game_pause == True:
                        self.icon = self.play_img
                        screen.blit(self.icon, self.text_rect)
                    else:
                        self.icon = self.pause_img
                        screen.blit(self.icon, self.text_rect)


timeBtn = TimeButton(130, 150, (655, NEXTTET_UPPER_GAP - 70),
                     playImg, pauseImg, (255, 65, 0))


class ExitButton:
    def __init__(self, text, width, height, pos, color, font):
        # global font
        self.top_rect = pg.Rect(pos, (width, height))
        self.top_color = color
        self.text = font.render(text, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.top_rect.center)

    def draw(self):
        pg.draw.rect(screen, self.top_color, self.top_rect, border_radius=4)
        screen.blit(self.text, self.text_rect)

    def click(self, event):
        global screen_looping
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    screen_looping = False


exitBtn = ExitButton("EXIT", 180, 60, (600, 560), (255, 0, 0), levelFont)


class ResetButton:
    def __init__(self, text, width, height, pos, color, font):
        # global font
        self.top_rect = pg.Rect(pos, (width, height))
        self.top_color = color
        self.text = font.render(text, True, WHITE)
        self.text_rect = self.text.get_rect(center=self.top_rect.center)

    def draw(self):
        pg.draw.rect(screen, self.top_color, self.top_rect, border_radius=4)
        screen.blit(self.text, self.text_rect)

    def click(self, event):
        global game_map, drop_pos, game_pause, game_point
        x, y = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    game_pause = False
                    for i in range(0, CELLS_ON_ROW * CELLS_ON_COL):
                        game_map[i] = 0
                        drop_pos = 5
                        game_point = 0


resetBtn = ResetButton("RESET", 180, 60, (520, 640), (255, 0, 0), levelFont)

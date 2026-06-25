#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./asset/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pg.mixer_music.load('./asset/Menu.mp3')
        pg.mixer_music.play(-1)
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, text= "Mountain", text_color= COLOR_ORANGE, text_center_pos= ((WIN_WIDTH / 2), 70))
            self.menu_text(50, text= "Shooter", text_color= COLOR_ORANGE, text_center_pos= ((WIN_WIDTH / 2), 110))


            for i in range(len(MENU_OPTION)):
                self.menu_text(20, text=MENU_OPTION[i], text_color=C_WHITE, text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))

            pg.display.flip()
        # Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Close Window
                    quit()  # end pygame
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
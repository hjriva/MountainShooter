#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pg.init()
        window = pg.display.set_mode(size=(600, 480))

    def run(self, ):
        print('Setup Start')

        print('Setup Finish')

        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            # Check for all events
           # for event in pg.event.get():
                #if event.type == pg.QUIT:
                    #pg.quit()  # Close Window
                        #quit()  # end pygame


#!/usr/bin/python
#-*- coding: utf-8 -*-

try:
    import pygame
    from pygame.locals import *
    from files import *
    from image import *
    from box_1 import Box_1
    from box_2 import Box_2
except:
    print 'Error importing modules required.'
    exit(0)



class Game():
    def __init__(self):
        pygame.init()
        self.run = True

        self.history = [[False, False, False],[False, False, False]]
        self.current = 0
        self.current_1 = 0
        self.current2 = 0
        self.current_2 = 0
        self.surface =  pygame.display.set_mode((800,600))
        pygame.display.set_caption('JOED - Jogos Educacionais - ALGOTEACH')

        #Images

        self.background = Image(self.surface, background)
        self.button_main= Image(self.surface, button_main)
        self.map = Image(self.surface, map)
        self.right_box_0 = Image(self.surface, right_box_0)
        self.selection = Image(self.surface, selection)
        self.selection_1 = Image(self.surface, selection_1)
        self.mouse = pygame.image.load(ball)

    def back_menu(self, event):
        if self.xy[0] > 25 and self.xy[0] < 110 and self.xy[1] > 480 and self.xy[1] < 520:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    try:
                        self.box_1.exit()
                    except:
                        pass
                    try:
                        self.box_2.exit()
                    except:
                        pass
                    self.current = 0
                    self.current_1 = 0
                    self.current2 = 0
                    self.current_2 = 0

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.run = False
            self.xy = pygame.mouse.get_pos()
            self.background.show()
            self.right_box_0.show()
            self.button_main.show((25, 480))
            self.map.show()

            #BICICLETARIO
            if self.current == 0 and self.current2 == 0 and self.xy[0] > 401 and self.xy[0] < 496 and self.xy[1] > 486 and self.xy[1] < 557:
                self.selection.show((398, 467))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.box_1 = Box_1(self.map, self.background, self.surface, self.right_box_0)
                            self.current = 1

            #ESTACIONAMENTO
            if self.current == 0 and self.current2 == 0 and self.xy[0] > 415 and self.xy[0] < 496 and self.xy[1] > 122 and self.xy[1] < 385:
                self.selection_1.show((415, 112))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.box_2 = Box_2(self.map, self.background, self.surface, self.right_box_0)
                            self.current2 = 1

            #VOLTAR
            if self.current == 1:# or self.current2 == 1:
                self.back_menu(event)
                if self.current_1 == 1:
                    self.box_1.show_help(self.xy, event)
                    self.box_1.show_exe_1()
                elif self.xy[0] > 650 and self.xy[0] < 754 and self.xy[1] > 390 and self.xy[1] < 408:
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            try:
                                self.box_1.exe_1()
                                self.current_1 = 1
                            except:
                                pass

            if (self.current_1 == 1):
                    if self.box_1.back_box_1(self.xy, event):
                        self.current_1 = 0
                    else:
                        
                        self.box_1.choice(self.xy, event)
                        self.box_1.check(self.xy, event)
                    if self.xy[0] > 650 and self.xy[0] < 754 and self.xy[1] > 438 and self.xy[1] < 456:
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                self.box_1.exe_1()

            if self.current2 == 1:
                self.back_menu(event)
                if self.current_2 == 1:
                    self.box_2.show_help(self.xy, event)
                    self.box_2.show_exe_1()
                elif self.xy[0] > 650 and self.xy[0] < 754 and self.xy[1] > 390 and self.xy[1] < 408:
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            try:
                                self.box_2.exe_1()
                                self.current_2 = 1
                            except:
                                pass

            if (self.current_2 == 1):
                    if self.box_2.back_box_1(self.xy, event):
                        self.current_2 = 0
                    else:
                        self.box_2.choice(self.xy, event)
                        self.box_2.check(self.xy, event)
                    if self.xy[0] > 650 and self.xy[0] < 754 and self.xy[1] > 438 and self.xy[1] < 456:
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                self.box_2.exe_1()

            if (event.type == KEYDOWN and event.key == K_F4):
                self.surface = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
            elif (event.type == KEYDOWN and event.key == K_F3):
                self.surface = pygame.display.set_mode((800,600))
            pygame.display.update()
game = Game()
game.loop()
pygame.quit()
exit()

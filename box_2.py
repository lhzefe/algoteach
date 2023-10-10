from files import *
from image import *
import pygame
from pygame.locals import *

class Box_2():
    def __init__(self, map, background, surface, menu):
        self.choices = []
        self.background = background
        self.surface = surface
        self.map = map
        self.menu = menu
        self.menu.switch_image(right_box_2)

        self.itens = []
        self.itens.append( Image(surface, 'car_exe_1/button 1.png', False, (254, 491)) )
        self.itens.append( Image(surface, 'car_exe_1/button 2.png', False, (341, 491)) )
        self.itens.append( Image(surface, 'car_exe_1/button 3.png', False, (170, 491)) )
        self.itens.append( Image(surface, 'car_exe_1/button 4.png', False, (425, 491)) )
        self.itens.append( Image(surface, 'car_exe_1/button ok.png', False, (700, 360)) )
        self.itens.append( Image(surface, 'car_exe_1/button back.png', False, (691, 492)) )
        self.itens.append( Image(surface, 'bike_exe_1/help.png', False, (170, 393)))

        self.itens_changed = []
        self.itens_changed.append( Image(surface, 'car_exe_1/x.png', False, (170, 491)) )
        self.itens_changed.append( Image(surface, 'car_exe_1/x.png', False, (341, 491)) )
        self.itens_changed.append( Image(surface, 'car_exe_1/x.png', False, (254, 491)) )
        self.itens_changed.append( Image(surface, 'car_exe_1/x.png', False, (425, 491)) )

        self.itens_highlight = []
        self.itens_highlight.append( Image(surface, 'car_exe_1/Highlight_button 1.png', False, (170, 491)) )
        self.itens_highlight.append( Image(surface, 'car_exe_1/Highlight_button 2.png', False, (341, 491)) )
        self.itens_highlight.append( Image(surface, 'car_exe_1/Highlight_button 3.png', False, (254, 491)) )
        self.itens_highlight.append( Image(surface, 'car_exe_1/Highlight_button 4.png', False, (425, 491)) )

        self.help = Image(surface, 'car_exe_1/balon_help.png', False)

    def exit(self, image = right_box_0):
        self.background.switch_image(background)
        self.menu.status = True
        self.map.status = True
        self.menu.switch_image(image)
        for x in self.itens:
            x.status = False

    def exe_1(self):
        self.choices =[]
        self.menu.status = False
        self.map.status = False
        self.background.switch_image(exe_1_box_2)
        for x in self.itens:
            x.status = True

    def show_exe_1(self):
        for x in self.itens:
            x.show()
        for x in self.itens_changed:
            x.show()
        for x in self.itens_highlight:
            x.show()

    def back_box_1(self, xy, event):
        if xy[0] > 691 and xy[0] < 765 and xy[1] > 492 and xy[1] < 543:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.background.switch_image(background)
                    self.menu.status = True
                    self.map.status = True
                    for x in self.itens:
                        x.status = False
                    return True

    def show_help(self, xy, event):
        self.help.show()
        if xy[0] > 170 and xy[0] < 244 and xy[1] > 393 and xy[1] < 442:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.help.status == True:
                        self.help.status = False
                    else:
                       self.help.status = True

    def choice(self, xy, event):
        if xy[1] > 491 and xy[1] < 540:
                    #Corrente
            if xy[0] > 254 and xy[0] < 330 and not 1 in self.choices:
                self.itens_highlight[2].status = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.choices.append(1)
                        self.itens_changed[2].status = True
                        print 1
            else:
                self.itens_highlight[2].status = False

                    #Bicicleta
            if xy[0] > 341 and xy[0] < 416 and not 2 in self.choices:
                self.itens_highlight[1].status = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.choices.append(2)
                        self.itens_changed[1].status = True
                        print 2
            else:
                self.itens_highlight[1].status = False

                    #Cadeado
            if xy[0] > 170 and xy[0] < 244 and not 3 in self.choices:
                self.itens_highlight[0].status = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.choices.append(3)
                        self.itens_changed[0].status = True
                        print 3
            else:
                self.itens_highlight[0].status = False

                    #Vaga
            if xy[0] > 425 and xy[0] < 500 and not 4 in self.choices:
                self.itens_highlight[3].status = True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.choices.append(4)
                        self.itens_changed[3].status = True
                        print 4
            else:
                self.itens_highlight[3].status = False
        else:
            for x in self.itens_highlight:
                x.status = False

    def check(self, xy, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if xy[0] > 700 and xy[0] < 754 and xy[1] > 360 and xy[1] < 414 and len(self.choices) == 4:
                    if self.choices == [3, 2, 4, 1]:
                        print 'PARABENS!!'
                    else:
                        print 'TENTE NOVAMENTE!!'
                    self.choices = []
                    for x in self.itens_changed:
                        x.status = False

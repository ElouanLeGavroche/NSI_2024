import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# Initialisation de Pygame
pygame.init()

import json

from game_render import Render
from Load import *

SCREEN_SIZE = 900, 400
FPS = 60

class main:
    def __init__(self):
        self.game = True
        self.menu = True

        self.screen = pygame.display.set_mode((SCREEN_SIZE), DOUBLEBUF | OPENGL)
        self.clock = pygame.time.Clock()

        self.images_list = []
        self.blocks_list = []
        self.ennemi_list = []

        self.render = Render()

    def init_point_off_view(self):

        # Initialisation de la vue
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, SCREEN_SIZE[0], SCREEN_SIZE[1], 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game = False

    def load_menu(self, menu):
        with open(f'assets/menu/{menu}.json', "r") as f:
            data = json.load(f)

        for i in data.values():
            if i["type"] == "Image":
                data = []

                if i["pos"] == [0,0]: data.append([0,0])
                else: data.append(i["pos"])

                if i["size"] == [0,0]: data.append([SCREEN_SIZE[0],SCREEN_SIZE[1]])
                else: data.append(i["size"])
                
            self.images_list.append((image_load(SCREEN_SIZE, i["path"]), data[0], data[1] ))

    def load_level(self, level):
        pass

    def update_game(self):
        self.init_point_off_view()

        self.load_menu('main_menu')
        while self.game:
            self.event()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            #afficher les éléments
            for i in self.images_list:
                print(i)
                self.render.draw_image(i[0], i[1][0], i[1][1], i[2][0], i[2][1])

            #afficher du textes
            self.render.draw_text(140, 120, f"{round(self.clock.get_fps())} FPS")

            if self.menu == True:
                pass
            else:
                pass
            
            pygame.display.flip()
            self.clock.tick(FPS)

Game = main()
Game.update_game()
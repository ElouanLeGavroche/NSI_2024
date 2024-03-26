import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Render:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 64)

    def draw_image(self, texture, x, y, width, height):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1)
        glVertex2f(x, y)
        glTexCoord2f(1, 1)
        glVertex2f(x + width, y)
        glTexCoord2f(1, 0)
        glVertex2f(x + width, y + height)
        glTexCoord2f(0, 0)
        glVertex2f(x, y + height)
        glEnd()
        glDisable(GL_TEXTURE_2D)

    def draw_text(self, x, y, text):
        textSurface = self.font.render(text, True, (0, 66, 0, 255)).convert_alpha()
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glRasterPos2d(x, y)  
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
import sys

import pygame
from config import *

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (0, 255, 0)
GREEN = (0, 179, 71)
CYAN = (7, 184, 255)
BLUE = (0, 0, 255)
PURPLE = (108, 70, 117)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MINT = (216, 249, 204)

RESOLUTION = (800, 500)


class Paint:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.screen.fill(WHITE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.color = BLACK
        self.radius = 3
        
        self.drawing = False
        self.end = []

        self.drawing_line = False
        self.drawing_rect = False
        self.drawing_circle = False

        #create top bar
        pygame.draw.rect(self.screen, BLACK, (0, 0, 800, 50))
        self.red_button = Button(self.screen, RED, 5, 5, 40, 40)
        self.orange_button = Button(self.screen, ORANGE, 50, 5, 40, 40)
        self.yellow_button = Button(self.screen, YELLOW, 95, 5, 40, 40)
        self.lightgreen_button = Button(self.screen, LIGHT_GREEN, 140, 5, 40, 40)
        self.green_button = Button(self.screen, GREEN, 185, 5, 40, 40)
        self.cyan_button = Button(self.screen, CYAN, 230, 5, 40, 40)
        self.blue_button = Button(self.screen, BLUE, 275, 5, 40, 40)
        self.purple_button = Button(self.screen, PURPLE, 320, 5, 40, 40)
        self.pen_button = Button(self.screen, CYAN, 500, 5, 80, 40, content='LÁPIZ')
        self.paint_button = Button(self.screen, MINT, 585, 5, 80, 40, content='PINTAR')
        self.clean_button = Button(self.screen, WHITE, 670, 5, 80, 40, content='LIMPIAR')
        self.x_button = Button(self.screen, RED, 755, 5, 40, 40, content='X', fontsize=40)

        #create left bar
        pygame.draw.rect(self.screen, BLACK, (0, 50, 70, 300))


    def createTopBar(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0, 800, 50))
        red_button = Button(self.screen, RED, 5, 5, 40, 40)
        orange_button = Button(self.screen, ORANGE, 50, 5, 40, 40)
        yellow_button = Button(self.screen, YELLOW, 95, 5, 40, 40)
        lightgreen_button = Button(self.screen, LIGHT_GREEN, 140, 5, 40, 40)
        green_button = Button(self.screen, GREEN, 185, 5, 40, 40)
        cyan_button = Button(self.screen, CYAN, 230, 5, 40, 40)
        blue_button = Button(self.screen, BLUE, 275, 5, 40, 40)
        purple_button = Button(self.screen, PURPLE, 320, 5, 40, 40)

    def createLeftBar(self):
        pygame.draw.rect(self.screen, BLACK, (0, 80, 50, 200))

    def scribbling(self, start, end):
        dx = end[0] - start[0]
        dy = end[1] - start [0]
        distance = max(abs(dx), abs(dy))

        for i in range(distance):
            x = int(start[0] + float(i) / distance * dx)
            y = int(start[1] + float(i) / distance * dy)
            pygame.draw.circle(self.screen, self.color, (x, y), self.radius)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if pygame.mouse.get_pressed()[0]:
                if len(self.end) == 0:
                    self.end.insert(0, event.pos)
                    self.end.insert(0, event.pos)

                self.end.insert(0, event.pos)
                self.end.pop()

                pygame.draw.line(self.screen, self.color, self.end[1], self.end[0], self.radius)

            #if event.type ==


    def mainLoop(self):
        while self.running:
            self.events()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if self.red_button.isPressed(mouse_pos, mouse_pressed):
                self.color = RED


            pygame.display.flip()



class Button:
    def __init__(self, surface, color, x, y, width, height, content=None, fontsize=24, font_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        pygame.draw.rect(surface, color, self.rect)

        if content != None:
            self.font = pygame.font.Font(None, fontsize)
            self.content = content

            self.text = self.font.render(self.content, True, font_color)
            self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
            self.image.blit(self.text, self.text_rect)
            surface.blit(self.image, self.rect)

    def isPressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

if __name__ == '__main__':
    paint = Paint()

    while paint.running:
        paint.mainLoop()

    pygame.quit()
    sys.exit()
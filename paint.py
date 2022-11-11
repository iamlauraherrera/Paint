import sys
import pygame

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
        self.color = RED

        self.width = 2

        self.state = 'PEN'
        self.unable_buttons = False

        self.points = []
        self.cont = 0

        # create top bar
        self.top_bar_rect = pygame.Rect(0, 0, 800, 50)
        self.top_bar = pygame.Surface(self.top_bar_rect.size)
        self.top_bar.fill(BLACK)
        self.screen.blit(self.top_bar, (self.top_bar_rect.x, self.top_bar_rect.y))

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

        self.x_button = Button(self.screen, RED, 755, 5, 40, 40, content='X', fontsize=40, font_color=WHITE)

        # create left bar
        self.left_bar_rect = pygame.Rect(0, 50, 64, 230)
        self.left_bar = pygame.Surface(self.left_bar_rect.size)
        self.left_bar.fill(BLACK)
        self.screen.blit(self.left_bar, (self.left_bar_rect.x, self.left_bar_rect.y))

        self.line_button = Button(self.screen, WHITE, 2, 50, 60, 60)
        pygame.draw.line(self.screen, BLACK, (6, 54), (56, 106), width=2)

        self.rect_button = Button(self.screen, WHITE, 2, 112, 60, 60)
        pygame.draw.rect(self.screen, BLACK, (6, 116, 52, 52), width=2)

        self.circle_button = Button(self.screen, WHITE, 2, 174, 60, 60)
        pygame.draw.circle(self.screen, BLACK, (32, 204), 28, width=2)

        self.width1_button = Button(self.screen, WHITE, 2, 236, 60, 20)
        pygame.draw.line(self.screen, BLACK, (6, 246), (56, 246), width=2)

        self.width2_button = Button(self.screen, WHITE, 2, 258, 60, 20)
        pygame.draw.line(self.screen, BLACK, (6, 268), (56, 268), width=4)

    # EVENTOS GENERALES
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == 'PEN':
                if pygame.mouse.get_pressed()[0]:
                    if len(self.points) == 0:
                        self.points.insert(0, event.pos)
                        self.points.insert(0, event.pos)

                    self.points.insert(0, event.pos)
                    self.points.pop()

                    pygame.draw.line(self.screen, self.color, self.points[1], self.points[0], self.width)

                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.unable_buttons = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.points = []
                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.unable_buttons = False

            if self.state == 'CLEAN':
                if pygame.mouse.get_pressed()[0]:
                    if len(self.points) == 0:
                        self.points.insert(0, event.pos)
                        self.points.insert(0, event.pos)

                    self.points.insert(0, event.pos)
                    self.points.pop()

                    pygame.draw.line(self.screen, WHITE, self.points[1], self.points[0], 10)

                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.unable_buttons = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.points = []
                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.unable_buttons = False

            elif self.state == 'LINE':
                if event.type == pygame.MOUSEBUTTONDOWN and self.cont == 0:
                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.points.append(event.pos)
                        self.cont += 1
                        self.unable_buttons = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.cont == 1:
                    self.points.append(event.pos)

                    pygame.draw.line(self.screen, self.color, self.points[0], self.points[1], self.width)

                    self.points = []
                    self.cont = 0
                    
                elif event.type == pygame.MOUSEBUTTONUP and self.cont == 0:
                    self.unable_buttons = False

            elif self.state == 'RECT':
                if event.type == pygame.MOUSEBUTTONDOWN and self.cont == 0:
                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.points.append(event.pos)
                        self.cont += 1
                        self.unable_buttons = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.cont == 1:
                    self.points.append(event.pos)

                    if self.points[0][0] < self.points[1][0]: x = self.points[0][0]
                    else: x = self.points[1][0]

                    if self.points[0][1] < self.points[1][1]: y = self.points[0][1]
                    else: y = self.points[1][1]

                    weight = abs(self.points[0][0] - self.points[1][0])
                    height = abs(self.points[0][1] - self.points[1][1])
                    pygame.draw.rect(self.screen, self.color, (x, y, weight, height), self.width)

                    self.points = []
                    self.cont = 0
                elif event.type == pygame.MOUSEBUTTONUP and self.cont == 0:
                    self.unable_buttons = False

            if self.state == 'CIRCLE':
                if event.type == pygame.MOUSEBUTTONDOWN and self.cont == 0:
                    if not self.top_bar_rect.collidepoint(event.pos) and not self.left_bar_rect.collidepoint(event.pos):
                        self.points.append(event.pos)
                        self.cont += 1
                        self.unable_buttons = True
                elif event.type == pygame.MOUSEBUTTONDOWN and self.cont == 1:
                    self.points.append(event.pos)

                    if self.points[0][0] < self.points[1][0]: x = self.points[0][0]
                    else: x = self.points[1][0]

                    if self.points[0][1] < self.points[1][1]: y = self.points[0][1]
                    else: y = self.points[1][1]

                    weight = abs(self.points[0][0] - self.points[1][0])
                    height = abs(self.points[0][1] - self.points[1][1])
                    pygame.draw.ellipse(self.screen, self.color, (x, y, weight, height), self.width)

                    self.points = []
                    self.cont = 0
                elif event.type == pygame.MOUSEBUTTONUP and self.cont == 0:
                    self.unable_buttons = False


    def update(self):
        #update top bar
        self.screen.blit(self.top_bar, self.top_bar_rect)

        self.red_button.update(self.screen)

        self.orange_button.update(self.screen)

        self.yellow_button.update(self.screen)

        self.lightgreen_button.update(self.screen)

        self.green_button.update(self.screen)

        self.cyan_button.update(self.screen)

        self.blue_button.update(self.screen)

        self.purple_button.update(self.screen)

        self.pen_button.update(self.screen)

        self.paint_button.update(self.screen)

        self.clean_button.update(self.screen)

        self.x_button.update(self.screen)

        #update left bar
        self.screen.blit(self.left_bar, self.left_bar_rect)

        self.line_button.update(self.screen)
        pygame.draw.line(self.screen, BLACK, (6, 54), (56, 106), width=2)

        self.rect_button.update(self.screen)
        pygame.draw.rect(self.screen, BLACK, (6, 116, 52, 52), width=2)

        self.circle_button.update(self.screen)
        pygame.draw.circle(self.screen, BLACK, (32, 204), 28, width=2)

        self.width1_button.update(self.screen)
        pygame.draw.line(self.screen, BLACK, (6, 246), (56, 246), width=2)

        self.width2_button.update(self.screen)
        pygame.draw.line(self.screen, BLACK, (6, 268), (56, 268), width=4)

        #update full screen
        pygame.display.flip()

    def mainLoop(self):
        while self.running:
            self.events()

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if not self.unable_buttons:
            # BARRA SUPERIOR
                if self.red_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = RED

                if self.orange_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = ORANGE

                if self.yellow_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = YELLOW

                if self.lightgreen_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = LIGHT_GREEN

                if self.green_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = GREEN

                if self.cyan_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = CYAN

                if self.blue_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = BLUE

                if self.purple_button.isPressed(mouse_pos, mouse_pressed):
                    self.color = PURPLE

                if self.pen_button.isPressed(mouse_pos, mouse_pressed):
                    self.state = 'PEN'
                    self.points = []

                if self.paint_button.isPressed(mouse_pos, mouse_pressed):
                    pass

                if self.clean_button.isPressed(mouse_pos, mouse_pressed):
                    self.state = 'CLEAN'

                if self.x_button.isPressed(mouse_pos, mouse_pressed):
                    self.screen.fill(WHITE)

            # BARRA LATERAL
                if self.line_button.isPressed(mouse_pos, mouse_pressed):
                    self.state = 'LINE'
                    self.points = []

                if self.rect_button.isPressed(mouse_pos, mouse_pressed):
                    self.state = 'RECT'
                    self.points = []

                if self.circle_button.isPressed(mouse_pos, mouse_pressed):
                    self.state = 'CIRCLE'
                    self.points = []

                if self.width1_button.isPressed(mouse_pos, mouse_pressed):
                    self.width = 2

                if self.width2_button.isPressed(mouse_pos, mouse_pressed):
                    self.width = 4

            self.update()


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

        self.content = content

        pygame.draw.rect(surface, color, self.rect)

        if self.content != None:
            self.font = pygame.font.Font(None, fontsize)
            self.content = content

            self.text = self.font.render(self.content, True, font_color)
            self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 2))
            self.image.blit(self.text, self.text_rect)
            surface.blit(self.image, self.rect)

    def isPressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

    def update(self, surface):
        surface.blit(self.image, self.rect)


if __name__ == '__main__':
    paint = Paint()

    while paint.running:
        paint.mainLoop()

    pygame.quit()
    sys.exit()

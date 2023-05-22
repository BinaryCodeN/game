import pygame

"""class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
"""

class Button:
    def __int__(self, width, height, innact_col, act_col):
        self.width = width()
        self.height = height
        self.innact_col = innact_col
        self.act_col = act_col

    #рисование кнопки на экране
    def draw(self, x, y, message, action = None):
        #цвет кнопки при наведении курсора
        mouse = pygame.mouse.get_pos()

        #параметры нахождения курсора
        if x < mouse[0] < x + self.width:
            if y< mouse[1] < y+self.height:
                pygame.draw.rect(screen, (23, 204, 50), (x, y) )












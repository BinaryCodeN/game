'''import pygame
#pygame.init()
import game_functions as gf

#игровое окно
wind = pygame.display.set_mode(400, 300)
pygame.display.set_caption('китайские шашки')

while True:
    gf.update_screen(screen)'''
import math

### меню для игры
'''
from pygame import *

init()
size = (800, 600)
screen = display.set_mode(size)
srift = font.SysFont('arial', 50)
class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
    def append_option(self, option, callback):
        self._option_surfaces.append(srift.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)
    def switch(self, direction):
        self._callbacks[self._current_option_index]()

    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i*option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

menu = Menu()
menu.append_option('Hello', lambda: print('Hello'))
menu.append_option('Quit', quit)

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_w: #движение вверх if W
                menu.switch(-1)
            elif e.key == K_s: #движение вниз if S
                menu.switch(1)
            elif e.key == K_SPACE: #активация выбранной опции меню
                menu.select()
                
    screen.fill((0, 0, 0))
    menu.draw(screen, 100, 100, 75)
    display.flip()
quit()
'''

import pygame
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

game_paused= False
font = pygame.font.SysFont('Times new roman', 40)
#цвет текста
TEXT_COL = (255, 255, 255)

#загрузка фото для фона
фон_img = pygame.image.load("venv/фон.jpg").convert()
bg_width = фон_img.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH/ bg_width)
# загрузка фото для кнопок
выбигр_img = pygame.image.load("venv/выберите_игру.jpg").convert_alpha()
вис_img = pygame.image.load("venv/виселица.jpg").convert_alpha()
бик_img = pygame.image.load("venv/б_и_к.jpg").convert_alpha()

#look_1 = pygame.transform.smoothscale(выбигр_img, (new_width, new_height))

#создание экземпляров кнопки на экране
resume_button = button.Button(20, 8, выбигр_img, 1)
вис_button = button.Button(270, 250, вис_img, 1)
бик_button = button.Button(270, 350, бик_img, 1)

# функция дизайна окна
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# цикл перед остановкой
run= True
while run:

    clock.tick(FPS)
    for i in range(0, tiles):
        screen.blit(фон_img, (i*bg_width, 0))


    #цвет окна
    #screen.fill((149, 138, 236))
    #screen.blit(())


    #функционал кнопок
    if game_paused == True:
        if resume_button.draw(screen):
            run = False
        if вис_button.draw(screen):
            game_paused = False
        if бик_button.draw(screen):
            run = False

    else:
        draw_text('Выход к основному меню', font, TEXT_COL, 190, 255)

    #handlear
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type== pygame.QUIT: #функция quit() используется для выхода из программы на Python
            run = False
    pygame.display.update()

pygame.quit()

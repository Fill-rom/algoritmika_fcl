import pygame
import time
from random import randint
pygame.init()
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)
'''создаём окно программы'''
back = (200, 255, 255)#цвет фона
mw = pygame.display.set_mode((500, 500))#окно программы
mw.fill(back)
clock = pygame.time.Clock()
'''класс прямоугольник'''
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
       self.rect = pygame.Rect(x, y, width, height) #прямоугольник
       self.fill_color = color
 
    def color(self, new_color):
       self.fill_color = new_color
 
    def fill(self):
       pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness): #обводка существующего прямоугольника
       pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
'''класс надпись'''
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
       self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
'''классы таймер и игровой счет'''
stime = time.time()
time = 10
score = 0
Time_1 = Label(50, 80, 50, 50, back)
Time_1.set_text('Время:', 40, DARK_BLUE)
Time_1.draw(0,0)
Time_2 = Label(50, 80, 50, 50, back)
Time_2.set_text('Время:', 40, DARK_BLUE)
Time_2.draw(0,0)
Time_3 = Label(50, 80, 50, 50, back)
Time_3.set_text('Время:', 40, DARK_BLUE)
Time_3.draw(0,0)
Time_4 = Label(50, 80, 50, 50, back)
Time_4.set_text('Время:', 40, DARK_BLUE)
Time_4.draw(0,0)
score_1 = Label(350, 80, 50, 50, back)
score_1.set_text('счет:', 40, DARK_BLUE)
score_1.draw(0,0)
score_2 = Label(415, 80, 50, 50, back)
score_2.set_text(score, 40, DARK_BLUE)
score_2.draw(0,0)
cards = []
num_cards = 4
x = 70
for i in range(num_cards):
   new_card = Label(x, 170, 70, 100, YELLOW)
   new_card.outline(BLUE, 10)
   new_card.set_text('CLICK', 26)
   cards.append(new_card)
   x = x + 100
wait=0
while True:
    if wait == 0:
        wait = 25
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if i + 1==click:
               cards[i].draw(10,30)
            else:
                cards[i].fill()
    else:
        wait -= 1
    ftime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for c in range (num_cards):
                if cards[c].collidepoint(x, y):
                    if c + 1 == click:
                        cards[c].color(GREEN)
                        score+=1
                        score_2.set_text(text = score)
                    else:
                        cards[c].color(RED)
                        score-=1
                cards[c].fill()
    pygame.display.update()
    clock.tick(50)

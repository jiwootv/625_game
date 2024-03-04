# this is 쌈@뽕 TextInput box!!

import pygame
import time
import re

SIZE = width, height = 640, 480
screen = pygame.display.set_mode(SIZE)

pygame.init()

class Textinput_box:
    def __init__(self, dest, root, maxlen):
        self.root = root
        self.text1 = ""
        self.font1 = pygame.font.SysFont('malgungothic', 35)
        self.img1 = self.font1.render(self.text1, True, (0, 0, 0))

        self.rect1 = self.img1.get_rect()
        self.rect1.topleft = dest
        self.cursor1 = pygame.Rect(self.rect1.topright, (3, self.rect1.height))
        self.maxlen = maxlen
    def draw(self):
        self.img1 = self.font1.render(self.text1, True, (255,255,255))
        self.rect1.size = self.img1.get_size()
        self.cursor1.topleft = self.rect1.topright
        self.root.blit(self.img1, self.rect1)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.root, (255, 255, 255), self.cursor1)
        pygame.display.update()

    def event(self, event):
        R = re.compile("[a-zA-Z]")
        R1 = re.compile("[0-9]")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(self.text1) > 0:
                    self.text1 = self.text1[:-1]
            elif self.maxlen != len(self.text1) and event.unicode != " " and R.match(event.unicode) and not R1.match(event.unicode):  # 영어만 입력가능, 숫자 불가능, 공백 불가능, 특수문자 불가능, 최대 maxlen까지로 길이 제한
                self.text1 += event.unicode



    def get(self):
        return self.text1

if __name__ == "__main__":
    running = True
    T = Textinput_box((20, 40), screen, 15)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            T.event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print(T.get())

        T.draw()

        screen.fill((0,0,0))

    pygame.quit()
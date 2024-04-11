import sys

import pygame

pygame.init()
DIR = "data\\"
if __name__ == "__main__": DIR = "..\\"

DEBUG = True


def eventset(r):
    global EVENT
    print("EVENT SETTING:", r)
    EVENT = r


class MsgBox:
    def __init__(self, screen, text, speed, soundtype, size, y=0):
        self.font = pygame.font.Font(DIR + "font\\DungGeunMo.otf", size)
        self.y = y
        self.root = screen
        self.P = True
        self.size = size
        self.text = text
        self.text.append("")
        self.now_text = ""
        self.now_text_count = 0
        print(self.text)
        self.text_line = 0
        self.text_maxline = self.text.__len__()

        self.text_speed = speed
        self.sound_type = soundtype
        self.text_on = True
        self.quit = False
        self.time = 0
        self.rect1 = pygame.Rect(25, 340, 590, 120)
        self.rect2 = pygame.Rect(30, 350, 580, 100)
        self.rect_t = []
        for i in self.text:
            self.rect_t.append(self.font.render(i, 1, (255, 255, 255)))
        print(self.rect_t)
        self.sound = [pygame.mixer.Sound(DIR + "sound\\effect\\A Piano.wav"), pygame.mixer.Sound(DIR + "sound\\effect"
                                                                                                       "\\Typing.wav", )]
        self.ev = 0
        self.draw()

    def t_update(self):
        self.rect_t = self.font.render(self.now_text, 1, (255, 255, 255))
        if not len(self.text[self.text_line]) == self.now_text_count or self.now_text_count == 0 and not self.text_on:
            print(self.text[self.text_line].__len__() == len(self.now_text))
            if DEBUG: print("------")

            self.now_text += self.text[self.text_line][self.now_text_count]
            self.now_text_count += 1
            if self.now_text_count != 0 and self.text[self.text_line][self.now_text_count - 1] != " ": self.sound[
                self.sound_type].play()
            if DEBUG:
                print("현재 글자:", self.now_text)
                print("현재 글자 순서:", self.now_text_count)
        if self.now_text.__len__() == self.text[self.text_line].__len__() and self.text_line + 1 == self.text_maxline:
            self.P = False
        elif self.text_line == self.text_maxline:
            self.now_text_count = 0
            self.now_text = ""

    def _draw(self) -> None:
        pygame.draw.rect(self.root, (255, 255, 255), self.rect1)
        pygame.draw.rect(self.root, (0), self.rect2)
        self.root.blit(self.rect_t, (15 + self.size, 323 + self.y + self.size))
# 아 왜 변경안됨 ;;
    def timer(self) -> None:
        self.time = pygame.time.get_ticks()

    def get_event(self) -> int:
        return self.quit


    def draw(self):
        clock = pygame.time.Clock()
        self.P = True
        while self.P:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quit = True
                    self.P = False

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_z or event.key == pygame.K_RETURN) and len(self.text[self.text_line]) == self.now_text_count:
                        if self.text_maxline != self.text_line:
                            self.text_on = True
                            self.text_line += 1
                            self.now_text_count = 0
                            self.now_text = ""
                        else:
                            self.P = False
                            clock.tick(30)
                    if event.key == pygame.K_x:
                        self.now_text = self.text[self.text_line]
                        self.now_text_count = len(self.text[self.text_line])
            self.t_update()
            self._draw()
            pygame.display.update()
            clock.tick(self.text_speed)
            pygame.display.update()


if __name__ == "__main__":
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480))
    if MsgBox(screen,
           ["1972년 11월 21일,", "김두한은 오랜 지병이었던 고혈압으로 쓰러졌다"],
           10, 0, 25).get_event():
        print("SAVING")

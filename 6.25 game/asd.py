import pygame
import time

SIZE = width, height = 640, 240

screen = pygame.display.set_mode(SIZE)
screen.fill((255, 255, 255))
pygame.init()

# Text Editing



running = True
class Textinput_box:
    def __init__(self, dest, root):
        self.root = root
        self.text1 = ""
        self.font1 = pygame.font.SysFont('malgungothic', 35)
        self.img1 = self.font1.render(self.text1, True, (0, 0, 0))

        self.rect1 = self.img1.get_rect()
        self.rect1.topleft = dest
        self.cursor1 = pygame.Rect(self.rect1.topright, (3, self.rect1.height))

    def draw(self):
        self.img1 = self.font1.render(self.text1, True, (0, 0, 0))
        self.rect1.size = self.img1.get_size()
        self.cursor1.topleft = self.rect1.topright
        self.root.blit(self.img1, self.rect1)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.root, (255, 0, 0), self.cursor1)
        pygame.display.update()

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(self.text1) > 0:
                    self.text1 = self.text1[:-1]
            else:
               self.text1 += event.unicode

T = Textinput_box((20, 40), screen)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        T.event(event)

    T.draw()

    screen.fill((255, 255, 255))



pygame.quit()

import sys

import pygame

pygame.init()
DIR = "data\\"
if __name__ == "__main__": DIR = "..\\"

DEBUG = False

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
		self.now_text = ""
		self.now_text_count = 0
		self.text_speed = speed
		self.sound_type = soundtype
		self.time = 0
		self.rect1 = pygame.Rect(25, 340, 590, 120)
		self.rect2 = pygame.Rect(30, 350, 580, 100)
		self.rect_t = self.font.render(self.text, 1, (255, 255, 255))
		self.sound = [pygame.mixer.Sound(DIR + "sound\\effect\\A Piano.wav")]
		self.ev = 0
		self.draw()

	def t_update(self):
		self.rect_t = self.font.render(self.now_text, 1, (255, 255, 255))
		if not len(self.text) == self.now_text_count or self.now_text_count == 0:
			if DEBUG: print("------")
			self.now_text += self.text[self.now_text_count]
			self.now_text_count += 1
			if self.now_text_count != 0: self.sound[self.sound_type].play()
			if DEBUG:
				print("현재 글자:", self.now_text)
				print("현재 글자 순서:", self.now_text_count)

	def _draw(self):
		pygame.draw.rect(self.root, (255, 255, 255), self.rect1)
		pygame.draw.rect(self.root, (0), self.rect2)
		self.root.blit(self.rect_t, (15 + self.size, 323 + self.y + self.size))

	def timer(self):
		self.time = pygame.time.get_ticks()

	def draw(self):
		clock = pygame.time.Clock()
		self.P = True
		while self.P:
			for event in pygame.event.get():
				EVENT(event)
				if event.type == pygame.QUIT:
					self.P = False
					clock.tick(30)
					return "END1"
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_z and len(self.text) == self.now_text_count:
						self.P = False
						clock.tick(30)
						return "END2"
					if event.key == pygame.K_x:
						self.now_text = self.text
						self.now_text_count = len(self.text)
						print("X")
			self.t_update()
			self._draw()
			pygame.display.update()
			clock.tick(self.text_speed)
			pygame.display.update()


if __name__ == "__main__":

	running = True
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((640, 480))
	while True:
		a = MsgBox(screen, "* 다람쥐가 헌 쳇바퀴를 타고파 하지 않는다..", 10, 0, 25).draw()
		if a == "END1":
			pygame.quit()
			sys.exit()
		elif a == "END2":
			if DEBUG: print("성공")
			break

	while True:
		a = MsgBox(screen, "엄마 꺵째이 지우", 20, 0, 25).draw()
		if a == "END1":
			pygame.quit()
			sys.exit()
		elif a == "END2":
			if DEBUG: print("성공")
			break

	while True:
		screen.fill(0)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if DEBUG: print("BER")
				sys.exit()

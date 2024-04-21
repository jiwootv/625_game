import pygame, sys

DIR = "..\\"
if not __name__ == "__main__": DIR = "data\\"

if __name__ == "__main__":
	import constants
else:
	import data.code.constants

print(constants.ROOM_NAMES)


def text_draw(surface, size, text, color, posx, posy, sort=0):
	font = pygame.font.Font(DIR + "font\\DungGeunMo.otf", size)
	t = font.render(text, True, color)
	if sort: surface.blit(t, (posx-t.get_size()[0], posy))
	else: surface.blit(t, (posx, posy))


class StatsBar:
	def __init__(self, screen, hp, room_number):
		self.screen = screen
		self.hp = hp
		self.rect = pygame.rect.Rect(620 - hp, 440, hp, 20)
		self.room_N = room_number

	def draw(self):
		self._drawNowRoom()
		self._drawStatusBar()

	def _drawNowRoom(self):
		t = "현재 위치 | "+constants.ROOM_NAMES[self.room_N]
		text_draw(self.screen, 30, t, (255, 255, 255), 0, 0)  # 620-t.__len__()*10,

	def _drawStatusBar(self):
		color = (255, 255, 255)
		h = self.hp // 10

		if h < 2:
			color = pygame.Color("red")
		elif h < 4:
			color = (200, 0, 0)
		elif h < 8:
			color = (255, 255, 0)
		text = "HP | {}".format(k)
		text_draw(self.screen, 20, text, color, 620, 420, sort=1)
		pygame.draw.rect(self.screen, color, self.rect)


pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
k = 100
roomnumber = 0
while True:
	# if k == 360: k = 0
	window.fill((0))
	S = StatsBar(window, k ,roomnumber)
	S.draw()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN and not k == 10:
				k -= 10
			if event.key == pygame.K_UP and not k == 200: k += 10
			if event.key == pygame.K_t:
				roomnumber += 1
			if event.key == pygame.K_g: roomnumber -= 1
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()
	pygame.display.update()
	clock.tick(30)
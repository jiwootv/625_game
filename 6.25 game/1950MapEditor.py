# 와 위대한 시작..
# 1950 게임 맵 에디터 메인 코드

import data.code.button as bt  # 절대 빼먹으면 안되는 것
import data.code.map as m_ap
import pygame
import sys

pygame.init()  # pygame 모듈 초기화


class Main:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.select_SE = pygame.mixer.Sound(r'data\sound\effect\A Piano.wav')
		self.collect_SE = pygame.mixer.Sound(r'data\sound\effect\Connect.wav')

		print("성공적으로 Main 클래스가 로드되었습니다")
		self.screen = pygame.display.set_mode((880, 660))  # 640, 480의 2배
		self.preview = pygame.rect.Rect(0, 0, 640, 480)
		self.preview1 = pygame.rect.Rect(0, 480, 640, 180)
		self.preview2 = pygame.rect.Rect(640, 0, 240, 660)
		self.clock = pygame.time.Clock()

		self.tile_size = 60
		self.map_max = 10
		# self.preview1 = pygame.rect.Rect(0, 0, 640, 480)
		self.Map_c = m_ap.Map(self.screen)
		self.file_index = 1
		self.select_IRID = 0

		self.saveButton = bt.Button(20, 600, pygame.image.load("data\\img\\save_btn.png"), 1)

		self.IRID_list = ["없음", "다음 방 이동"]
		pygame.display.set_caption("1950 Map Editor")
		self.text = lambda size, text, color, x, y: self.screen.blit(
			pygame.font.Font(r"data\font\DungGeunMo.otf", size).render(text, 1, color), (x, y))
		self.x, y = 0, 0

	def draw_preview(self):
		pygame.draw.rect(self.screen, (0, 0, 0), self.preview)

	def draw_hider(self):
		self.x, self.y = list(map(lambda x: x//self.tile_size, pygame.mouse.get_pos()))
		print(self.x, self.y)
		self.tile_rect1, self.tile_rect2 = pygame.rect.Rect(self.x*self.tile_size, self.y*self.tile_size, self.tile_size, self.tile_size), pygame.rect.Rect(self.x*self.tile_size+5, self.y*self.tile_size+5, self.tile_size-5, self.tile_size-5)
		pygame.draw.rect(self.screen, (255, 255, 255), self.tile_rect1)
		#pygame.draw.rect(self.screen, (255, 255, 255), self.tile_rect2)
		pygame.draw.rect(self.screen, (0, 0, 70), self.preview1)
		pygame.draw.rect(self.screen, (0, 0, 70), self.preview2)

	def lines(self):
		for k in range(0, self.map_max * self.tile_size + 1, self.tile_size):  # 가로선
			x, y = self.Map_c.moveposGet()
			pygame.draw.line(self.screen, (255, 255, 255), start_pos=(x, k + y), end_pos=(x+self.map_max*self.tile_size, k + y))

		for k in range(0, self.map_max * self.tile_size + 1, self.tile_size):  # 가로선
			x, y = self.Map_c.moveposGet()
			pygame.draw.line(self.screen, (255, 255, 255), start_pos=(k+x, y), end_pos=(k+x, self.map_max * self.tile_size+y))

	def event(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_i:
					self.select_IRID += 1
					self.select_SE.play()
				if event.key == pygame.K_k and not self.select_IRID == 0:
					self.select_IRID -= 1
					self.select_SE.play()
				if event.key == pygame.K_UP:
					self.file_index += 1
					self.select_SE.play()
				if event.key == pygame.K_DOWN and not self.file_index == 0:
					self.file_index -= 1
					self.select_SE.play()

		# 버튼 드로우
		if self.saveButton.draw(self.screen): print("Click")

	def run(self):
		self.Map_c._load(1)
		self.Map_c.draw_set()
		self.Map_c.brickPassSet(1)
		while True:

			self.screen.fill((0, 0, 0))
			try:
				a = self.IRID_list[self.select_IRID]
			except:
				a = "존재하지 않는 IRID"

			self.draw_preview()
			self.Map_c.draw()
			self.Map_c.event()
			self.lines()
			self.draw_hider()

			self.event()
			self.text(30, "현재 파일 번호: %d" % self.file_index, (255, 255, 255), 600, 600)
			self.text(30, a, (255, 255, 255), 600, 550)
			self.text(30, "현재 IRID: %d" % self.select_IRID, (255, 255, 255), 600, 500)

			pygame.display.update()
			self.clock.tick(60)


M = Main()
M.run()

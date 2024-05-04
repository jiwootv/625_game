import pygame, sys, math, random
pygame.init()
screen = pygame.display.set_mode((640, 480))
k =0
clock = pygame.time.Clock()
x = random.randint(200, 400)
class Test:
	def __init__(self, screen):
		self.count = 0
		self.screen = screen
		self.r_c = int(random.random()*255)

		self.color = (int(random.random()*255), int(random.random()*255), int(random.random()*255))
		print(self.color)
		self.x = self.x = random.randint(0, 600)
		self.x = self.x = random.randint(0, 600)
	def draw(self):
		self.count += 0.1
		if math.tan(self.count + 0.5) * 20 > 300:
			print("GAY", self.count)
			self.x = random.randint(0, 600)
			self.count = 4.2

		pygame.draw.rect(screen, self.color, pygame.rect.Rect(self.x, 200 + math.tan(self.count + 0.5) * 20, 40, 60))
for i in range(input()): print(i+1)
tanmak = []
for i in range(0): tanmak.append(Test(screen))
while True:
	k += 0.1
	screen.fill(0)
	pygame.draw.rect(screen, (255, 0, 255), pygame.rect.Rect(300, 200+math.sin(k)*20, 40, 40))
	pygame.draw.rect(screen, (255, 0, 255), pygame.rect.Rect(340, 200 + math.sin(k-0.5) * 20, 40, 40))
	pygame.draw.rect(screen, (255, 0, 255), pygame.rect.Rect(380, 200 + math.sin(k - 1) * 20, 40, 40))
	pygame.draw.rect(screen, (255, 0, 255), pygame.rect.Rect(260, 200 + math.sin(k+0.5) * 20, 40, 40))


	for t in tanmak:
		t.draw()
		pass


	for i in range(1):
		a = pygame.rect.Rect((math.cos(k + 0.5 + i*0.25) * 60+320, math.sin(k + 0.5 + i*0.25) * 60+200, 40, 40))
		#pygame.draw.rect(screen, (0, 0, 255), a)
		pygame.draw.circle(screen, (200, 150, 0), (math.cos(k + 0.5 + i*0.25) * 120+320, math.sin(k + 0.5 + i*0.25) * 60+200), 40)
		print(k)

		k += random.random()*0.2



	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	clock.tick(30)
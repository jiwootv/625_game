import pygame, sys

pygame.init()
pygame.mixer.init()
DIR = "data\\"
if __name__ == '__main__': DIR = "..\\"
class Gun:
	def __init__(self):
		self.no_bullet_sound = pygame.mixer.Sound(DIR + "sound\\effect\\Shot0.wav")
		self.gun_sound = pygame.mixer.Sound(DIR + "sound\\effect\\Rebolber1.mp3")
		self.gun_sound.set_volume(0.25)
		#self.gun_sound.play()
		self.no_bullet_sound.play()
		self.gun_images = []



if __name__ == "__main__":
	pygame.init()
	window = pygame.display.set_mode((640, 480))
	clock = pygame.time.Clock()
	G = Gun()
	while True:
		window.fill(0)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		clock.tick(30)
		pygame.display.update()
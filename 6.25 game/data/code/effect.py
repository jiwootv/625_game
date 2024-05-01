import pygame, msgbox
import sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Constants for screen dimensions and frame rate
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Set up the window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Clock to manage frame rate
clock = pygame.time.Clock()
DIR = "data\\sound"
if __name__ == '__main__': DIR = "..\\sound"


class GameOver:
	def __init__(self, screen):
		self.game_over_sounds = [pygame.mixer.Sound(DIR + r"\music\Myuu-Down-the-Rabbit-hole.mp3"), pygame.mixer.Sound(r"..\sound\effect\GlassBroken.mp3"), pygame.mixer.Sound(r"..\sound\effect\HandGunSound1.mp3")]
		self.game_over_sounds[2].play()
		self.game_over_sounds[1].play()
		self.game_over_sounds[0].play(-1)
		self.t123 = pygame.time.get_ticks()
		self.soundcount = 0
		print(self.t123)
		self.connect = pygame.mixer.Sound(r"..\sound\effect\Connect.wav")
		self.screen = screen



		self.text = lambda size, text, pos: self.screen.blit(pygame.font.Font(r"..\font\DungGeunMo.otf", 50).render(text, 0, (255, 255, 255)), pos)
		self.text1 = self.text(30, "GaNaDaLaMaBaSa", (0, 0))
		#self.connect.play()
		print(DIR + "\\effect\\A piano.wav")

	def text_show(self):
		self.t = pygame.time.get_ticks()
		if self.t> 3000 + self.t123:
			if not self.soundcount: self.connect.play()
			self.soundcount = 1
			self.text(30, "Retry?", (200, 250))
		self.text(30, "Game Over", (200, 210))



# Cinematic techniques
class FadeInOut:
	def __init__(self, screen):
		self.screen = screen
		self.fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.fade_surface_rect = self.fade_surface.get_rect()
		print()
	def fade_in(self, color, speed):
		'''Perform a fade-in effect on a given surface.'''
		for alpha in range(0, 255, speed):
			self.fade_surface.fill(color)
			#self.screen.fill(BLACK)
			self.fade_surface.set_alpha(alpha)
			self.screen.blit(self.fade_surface, self.fade_surface_rect)
			pygame.display.update()
			clock.tick(FRAMES_PER_SECOND)
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					return 1


	def fade_out(self, color, speed):
		'''Perform a fade-out effect on a given surface.'''
		for alpha in range(255, -1, -speed):
			self.screen.fill(BLACK)
			self.fade_surface.fill(color)
			self.fade_surface.set_alpha(alpha)
			self.screen.blit(self.fade_surface, self.fade_surface_rect)
			pygame.display.update()
			clock.tick(FRAMES_PER_SECOND)
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					return 1


	# Main function to execute cinematic effects

	def fade_in_out(self, color, speed):
		return self.fade_in(color, speed) or self.fade_out(color, speed)


# Run the program
if __name__ == '__main__':
	TYPE = 2
	if TYPE == 1:
		a = FadeInOut(window)

		running = True
		while running:


			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

			# Black screen to start with
			window.fill(BLACK)
			window.fill((25, 52, 255))
			pygame.display.update()

			# Fade in to white screen
			if a.fade_in_out(BLACK, 10): print("SAVING..")

			running = False  # Run the effect once for demo purposes
	if TYPE == 2:
		a = FadeInOut(window)
		# "붉은 액체가 머리를 타고 흘러내린다.", "서서히 눈이 감긴다. 졸리다.", "끝인.. 건가?"
		if msgbox.MsgBox(window, ["교촌치킨 허니콤보 먹고싶다..", "졸리다.."], 10, 0, 25).get_event(): print("SAVING..")
		g = GameOver(window)
		running = True
		window.fill((255, 255, 255))
		if a.fade_out((255, 0, 0), 10):
			print("SAVING..")
			sys.exit()


		while running:


			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

			# Black screen to start with
			window.fill(BLACK)
			g.text_show()
			pygame.display.update()

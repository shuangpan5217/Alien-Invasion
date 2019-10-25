import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self, screen, ai_settings):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/alien_ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def check_edges(self):
		if self.rect.right >= self.screen.get_rect().right:
			return True
		elif self.rect.left <= self.screen.get_rect().left:
			return True
		else:
			return False
	def update(self):
		self.x = self.x + self.ai_settings.alien_speed * self.ai_settings.fleet_direction
		self.rect.x = self.x 
	#	print(self.ai_settings.fleet_direction)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

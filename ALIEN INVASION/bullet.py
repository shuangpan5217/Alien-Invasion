import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ai_settings, ship, screen):
		super().__init__()
		self.screen = screen

		#create a bullet rect at (0, 0) and then set corrent position
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

		self.rect.centerx = ship.rect.centerx
	#	self.rect.top = ship.rect.top + ai_settings.bullet_height
		self.rect.bottom = ship.rect.bottom

		self.centery = float(self.rect.centery)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		self.centery = self.centery - self.speed_factor
		self.rect.centery = self.centery

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

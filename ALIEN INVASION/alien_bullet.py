import pygame
from pygame.sprite import Sprite
class AlienBullet(Sprite):
	def __init__(self, screen, alien, ai_setting, ship):
		super().__init__()
		self.ship = ship
		self.screen = screen
		self.alien = alien
		self.rect = pygame.Rect(0, 0, ai_setting.alien_bullet_width, ai_setting.alien_bullet_height)
		self.rect.centerx = self.alien.rect.centerx
		self.rect.bottom = self.alien.rect.bottom
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		self.color = ai_setting.alien_bullet_color
		self.speed = ai_setting.alien_bullet_speed
		self.ship_centerx = self.ship.center1
		self.ship_centery = self.ship.center2

	def update(self):
		self.centery = self.centery + self.speed
		if self.ship_centery - self.rect.centery > 0:
			self.centerx = self.speed * ((self.ship_centerx - self.rect.centerx) / (self.ship_centery - self.rect.centery)) + self.centerx
		self.rect.centery = self.centery
		self.rect.centerx = self.centerx

	def draw_alien_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_setting, screen):
		"""Initialize the ship and set its starting position"""
		super().__init__()
		self.screen = screen
		self.ai_setting = ai_setting

		#Load the ship image and get its rect
		self.image = pygame.image.load('images/my_ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		#start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.bottom - self.rect.bottom / 2
		self.rect.bottom = self.screen_rect.bottom / 2 + self.rect.bottom / 2
		self.center1 = float(self.rect.centerx)
		self.center2 = float(self.rect.centery)
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def center_ship(self):
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center1 = float(self.rect.centerx)
		self.center2 = float(self.rect.centery)

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center1 += self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center1 -= self.ai_setting.ship_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.center2 -= self.ai_setting.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.center2 += self.ai_setting.ship_speed_factor
		self.rect.centerx = self.center1
		self.rect.centery = self.center2
	#	print(self.rect.centerx)

import pygame
class Background():
	def __init__(self, screen):
		self.screen = screen
		self.my_background = pygame.image.load('images/alien.bmp')
		self.rect = self.my_background.get_rect()
		self.screen_rect = self.screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
	def blitme(self):
		self.screen.blit(self.my_background, self.rect)

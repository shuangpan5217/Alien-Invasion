import pygame.font
import pygame
class Button():
	def __init__(self, screen, message):
		"""Initilize button attributes"""
		self.screen = screen
		#set the dimensions and properties of button.

		self.width = 200
		self.height = 50

		self.button_color = (0, 0, 0)
		self.text_color = (255, 255, 255)

		self.font = pygame.font.SysFont(None, 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen.get_rect().center

		self.pre_message(message)

	def pre_message(self, message):
		self.text_image = self.font.render(message, True, self.text_color, self.button_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw_button(self):
		#self.screen.fill(self.button_color, self.rect)
		pygame.draw.rect(self.screen, self.button_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)
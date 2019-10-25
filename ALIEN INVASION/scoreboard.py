import pygame
import pygame.font
from ship import Ship
from pygame.sprite import Group

class ScoreBoard():
	def __init__(self, screen, stats, ai_settings):
		self.ai_settings = ai_settings
		self.screen = screen
		self.stats = stats
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 32)
		self.font2 = pygame.font.SysFont(None, 32)
		self.font3 = pygame.font.SysFont(None, 32)

		self.pre_score()
		self.pre_highest_score(stats, ai_settings)
		self.pre_level(stats)
		self.pre_ship(stats, ai_settings, screen)

	def pre_score(self):
		round_score = int(round(self.stats.score, -1))
		score = "{:,}".format(round_score)

		self.score_image = self.font.render("Score: " + score, True, self.text_color)
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.top = self.screen.get_rect().top + 20
		self.score_image_rect.right = self.screen.get_rect().right - 20

	def pre_highest_score(self, stats, ai_settings):
		round_score = int(round(self.stats.highest_score, -1))
		score = "{:,}".format(round_score)
		self.highest_score_image = self.font2.render("Highest score: " + score, True, self.text_color)
		self.highest_score_image_rect = self.highest_score_image.get_rect()
		self.highest_score_image_rect.top = self.screen.get_rect().top + 20
		self.highest_score_image_rect.centerx = ai_settings.screen_width / 2

	def pre_level(self, stats):
		self.level_image = self.font3.render("Level: " + str(stats.level), True, self.text_color)
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.top = self.screen.get_rect().top + 40
		self.level_image_rect.right = self.screen.get_rect().right - 20

	def pre_ship(self, stats, ai_settings, screen):
		ships = Group()
		self.ships = ships
		for ship_number in range(self.stats.life_left):
			ship = Ship(ai_settings, screen)
			ship.rect.x = ship.rect.width * ship_number
			ship.rect.y = 20
			ships.add(ship)

	def show_score(self):
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.highest_score_image, self.highest_score_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.ships.draw(self.screen)
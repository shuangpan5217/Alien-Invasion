class Settings():
	""" A class to store all settings for Alien Invasion"""
	def __init__(self):
		self.screen_width = 1024
		self.screen_height = 768
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 10.5

		#bullet settings
		self.bullet_speed_factor = 40.5
		self.bullet_width = 2
		self.bullet_height = 50
		self.bullet_color = (255, 255, 255)
		self.bullet_allowed = 10
		self.alien_bullet_width = 2
		self.alien_bullet_height = 10
		self.alien_bullet_speed = 2
		self.alien_bullet_color = (0, 0, 0)
		#continue shooting
		self.continue_shooting = False
		self.alien_speed = 4
		self.drop_speed = 5
		self.fleet_direction = 1

		self.alien_score_factor = 1.5
		
		#total lives
		self.life_left = 3

	def init_dynamic_setting(self):
		self.bullet_speed_factor = 40.5
		self.ship_speed_factor = 10.5
		self.alien_speed = 4
		self.drop_speed = 5
		self.fleet_direction = 1
		self.alien_bullet_speed = 2

	def increase_speed(self, stats, alien_bullets):
		self.ship_speed_factor += 1
		self.bullet_speed_factor += 1
		stats.alien_point = int(stats.alien_point * self.alien_score_factor)
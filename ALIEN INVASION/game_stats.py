
class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.life_left = self.ai_settings.life_left
		self.game_active = False
		self.alien_point = 50
		self.highest_score = 0

	def reset_stats(self):
		self.life_left = self.ai_settings.life_left
		self.score = 0
		self.level = 1
		self.score = 0
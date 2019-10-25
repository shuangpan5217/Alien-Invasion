import pygame
class Music():
	def __int__(self):
		pygame.mixer.init()

	def start_play(self):
		pygame.mixer.music.load('music/star_war.mp3')
		pygame.mixer.music.play(5, 0.0)
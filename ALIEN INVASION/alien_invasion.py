import images
import pygame
from settings import Settings
from background import Background 
from ship import Ship
from music import Music
from aliens import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from game_stats import GameStats
from alien_bullet import AlienBullet

def run_game():
	#initialize game and create a screen object
	pygame.init()
	ai_settings = Settings() 
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#make a ship
	ship = Ship(ai_settings, screen)  
	#make an alien
	aliens = Group()
	#gf.create_fleet(ai_settings, screen, aliens, ship)
	#make bullet sprites group
	bullets = Group() 
	#create alien bullet group
	alien_bullets = Group()
	#make screen background
	background = Background(screen) 
	#add music to the game
	music = Music()
	#start play
	music.start_play() 
	#create statics
	stats = GameStats(ai_settings)
	stats.reset_stats()
	with open("highest_score.txt", 'r') as hs:
		highestscore = hs.readline()
	stats.highest_score = int(highestscore)
	#create play button
	play_button = Button(screen, "Play") 
	#initlize score board
	score_board = ScoreBoard(screen, stats, ai_settings)

	#Start the main loop for the game.
	while True:

		#watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, score_board, alien_bullets)
		if stats.game_active:
			gf.update_ship(ship)
			gf.update_bullets(bullets, aliens, ai_settings, ship, screen, stats, score_board, alien_bullets )
			gf.update_alien_bullets(alien_bullets, ship, stats, aliens, bullets, screen, ai_settings, score_board)
			gf.update_aliens(aliens, ai_settings, ship, stats, bullets, screen, score_board, alien_bullets)
		gf.update_screen(ai_settings, screen, ship, bullets, background, aliens, play_button, stats, score_board, alien_bullets)

run_game()      
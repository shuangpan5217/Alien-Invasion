import sys
import pygame
from bullet import Bullet
from aliens import Alien
from time import sleep
from alien_bullet import AlienBullet

def check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, score_board, alien_bullets):
	"""Respond to keypresses and mouse events"""
	continue_shooting(ai_settings, screen, ship, bullets)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			with open("highest_score.txt", 'w') as hs:
				hs.write(str(stats.highest_score))
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, ship, ai_settings, bullets, screen, aliens, stats, score_board, alien_bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, ship, ai_settings)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x = pygame.mouse.get_pos()[0]
			mouse_y = pygame.mouse.get_pos()[1]
			check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, score_board, alien_bullets)

def check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship, score_board, alien_bullets):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		ai_settings.init_dynamic_setting()
		stats.reset_stats()
		score_board.pre_score()
		score_board.pre_level(stats)
		score_board.pre_highest_score(stats, ai_settings)
		score_board.pre_ship(stats, ai_settings, screen)
		stats.game_active = True
		pygame.mouse.set_visible(False)

		aliens.empty()
		bullets.empty()
		alien_bullets.empty()

		create_fleet(ai_settings, screen, aliens, ship)
		create_alien_bullets(aliens, screen, stats, ai_settings, alien_bullets, ship)
		ship.center_ship()

def check_keydown_event(event, ship, ai_settings, bullets, screen, aliens, stats, score_board, alien_bullets):
	if event.key == pygame.K_ESCAPE:
		with open("highest_score.txt", 'w') as hs:
			hs.write(str(stats.highest_score))
		sys.exit()
	if event.key == pygame.constants.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.constants.K_LEFT:
		ship.moving_left = True                                    
	if event.key == pygame.K_UP:
		ship.moving_up = True
	if event.key == pygame.K_DOWN:
		ship.moving_down = True
	if event.key == pygame.K_SPACE:
		fire_bullets(ai_settings, ship, screen, bullets)
	if event.key == pygame.constants.K_p:
		use_p_start_game(stats, aliens, bullets, ship, ai_settings, screen, score_board, alien_bullets)

def check_keyup_event(event, ship, ai_settings):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_UP:
		ship.moving_up = False
	if event.key == pygame.K_DOWN:
		ship.moving_down = False
	if event.key == pygame.K_SPACE:
		ai_settings.continue_shooting = False

def use_p_start_game(stats, aliens, bullets, ship, ai_settings, screen, score_board, alien_bullets):
	if not stats.game_active:
		ai_settings.init_dynamic_setting()
		stats.reset_stats()
		score_board.pre_score()
		score_board.pre_level(stats)
		score_board.pre_highest_score(stats, ai_settings)
		score_board.pre_ship(stats, ai_settings, screen)
		stats.game_active = True
		pygame.mouse.set_visible(False)

		aliens.empty()
		bullets.empty()
		alien_bullets.empty()

		create_fleet(ai_settings, screen, aliens, ship)
		create_alien_bullets(aliens, screen, stats, ai_settings, alien_bullets, ship)
		ship.center_ship()

def continue_shooting(ai_settings, screen, ship, bullets):
	if ai_settings.continue_shooting and len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, ship, screen)
		bullets.add(new_bullet)
		pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/gun_shot.wav'))

def fire_bullets(ai_settings, ship, screen, bullets):
	ai_settings.continue_shooting = True
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, ship, screen)
		bullets.add(new_bullet)
		pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/gun_shot.wav'))

def get_avaliable_alien(ai_settings, screen):
	alien = Alien(screen, ai_settings)
	alien_width = alien.rect.width
	avaliable_alien_space = ai_settings.screen_width - 2 * alien_width
	avaliable_alien = int(avaliable_alien_space / alien_width / 2)
	return avaliable_alien

def get_number_rows(ai_settings, screen, ship):
	alien = Alien(screen, ai_settings)
	alien_height = alien.rect.height
	avaliable_height_space = ai_settings.screen_height - 3 * alien_height - ship.rect.height
	avaliable_row = int(avaliable_height_space / alien_height / 2)
	return avaliable_row

def create_alien(number_aliens, screen, ai_settings, aliens, row_number):
	for alien_number in range(number_aliens):
		alien = Alien(screen, ai_settings)
		alien.x = alien.rect.width + alien.rect.width * 2 * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):
	number_aliens = get_avaliable_alien(ai_settings, screen)
	avaliable_row = get_number_rows(ai_settings, screen, ship)
	for row_number in range(avaliable_row):
		create_alien(number_aliens, screen, ai_settings, aliens, row_number)

def create_alien_bullets(aliens, screen, stats, ai_settings, alien_bullets, ship):
	for alien in aliens:
		alien_bullet = AlienBullet(screen, alien, ai_settings, ship)
		alien_bullets.add(alien_bullet)

def check_fleet_edges(aliens, ai_settings):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens, ai_settings)
			break
def change_fleet_direction(aliens, ai_settings):
	for alien in aliens.sprites():
		alien.rect.y = alien.rect.y + ai_settings.drop_speed
	ai_settings.fleet_direction *= -1
	#	print(ai_settings.fleet_direction)

def update_ship(ship):
	ship.update()

def check_highest_score(stats, score_board, ai_settings):
	if stats.highest_score < stats.score:
		stats.highest_score = stats.score
		score_board.pre_highest_score(stats, ai_settings)

def check_collision(ai_settings, aliens, bullets, screen, ship, stats, score_board, alien_bullets):
	collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
	for alien in collisions.values():
		stats.score += stats.alien_point
		score_board.pre_score()
	check_highest_score(stats, score_board, ai_settings)
	if len(aliens) == 0:
		bullets.empty()
		stats.level += 1
		score_board.pre_level(stats)
		ai_settings.alien_speed = ai_settings.alien_speed * 1.2
		ai_settings.drop_speed = ai_settings.drop_speed * 1.2
		ai_settings.increase_speed(stats, alien_bullets)
		create_fleet(ai_settings, screen, aliens, ship)

def update_bullets(bullets, aliens, ai_settings, ship, screen, stats, score_board, alien_bullets):
	bullets.update()
	for bullet in bullets.sprites():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_collision(ai_settings, aliens, bullets, screen, ship, stats, score_board, alien_bullets)

def check_alien_bullets_edges(alien_bullets):
	for alien_bullet in alien_bullets:
		if alien_bullet.rect.right >= alien_bullet.screen.get_rect().right:
			alien_bullets.remove(alien_bullet)
		elif alien_bullet.rect.left <= alien_bullet.screen.get_rect().left:
			alien_bullets.remove(alien_bullet)

def update_alien_bullets(alien_bullets, ship, stats, aliens, bullets, screen, ai_settings, score_board):
	check_alien_bullets_edges(alien_bullets)
	alien_bullets.update()
	collision_alien_bullet = pygame.sprite.spritecollideany(ship, alien_bullets)
	if collision_alien_bullet != None:
		alien_bullets.remove(collision_alien_bullet)
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, alien_bullets)
	check_alien_bullets_bottom(alien_bullets, screen, stats, ai_settings, aliens, ship)

def check_alien_bullets_bottom(alien_bullets, screen, stats, ai_settings, aliens, ship):

	for alien_bullet in alien_bullets:
		if alien_bullet.rect.bottom >= screen.get_rect().bottom:
			alien_bullets.remove(alien_bullet)
			print(len(alien_bullets))
	if(len(alien_bullets) == 0):
		ai_settings.alien_bullet_speed += 1
		create_alien_bullets(aliens, screen, stats, ai_settings, alien_bullets, ship)

def ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, alien_bullets):
	#print(stats.life_left)
	if stats.life_left > 0:
		stats.life_left-= 1

	#	aliens.empty()
	#	bullets.empty()
		score_board.pre_ship(stats, ai_settings, screen)
		#create_fleet(ai_settings, screen, aliens, ship)
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_alien_bottom(aliens, screen, bullets, ai_settings, ship, stats, score_board):
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen.get_rect().bottom:
			ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board)
			break

def update_aliens(aliens, ai_settings, ship, stats, bullets, screen, score_board, alien_bullets):
	check_fleet_edges(aliens, ai_settings)
	aliens.update()
	collision_alien = pygame.sprite.spritecollideany(ship, aliens)
	if collision_alien != None:
		aliens.remove(collision_alien)
		ship_hit(stats, aliens, bullets, ship, screen, ai_settings, score_board, alien_bullets)
	check_alien_bottom(aliens, screen, bullets, ai_settings, ship, stats, score_board)

def update_screen(ai_settings, screen, ship, bullets, background, aliens, play_button, stats, score_board, alien_bullets):
	# Redraw the screen during each pass through the loop
	background.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	for alien_bullet in alien_bullets:
		alien_bullet.draw_alien_bullet()
	if stats.game_active == False:
		play_button.draw_button()
	score_board.show_score()
	#make the most recently drawn screen visible
	pygame.display.flip()

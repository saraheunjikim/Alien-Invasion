import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invastion")
	
	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")
	
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# Make a ship.
	ship = Ship(ai_settings, screen)

	# Make a group to store bullets in.
	bullets = Group()
	aliens = Group()
	
	# Creat the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Set the background color.
	bg_color = (230, 230, 230)
	
	# Make an alien.
	alien = Alien(ai_settings, screen)
	
	# Start the main loop for the game.
	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
						aliens, bullets)
						
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		
		# Redraw the screen during each pass through the loop.
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
						play_button)
		

run_game()

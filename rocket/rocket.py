import sys
import pygame

from settings import Settings
from rock import Rock
import game_functions as gf
from pygame.sprite import Group
from star import Star


def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	rk_settings = Settings()
	screen = pygame.display.set_mode((rk_settings.screen_width, rk_settings.screen_height))
	pygame.display.set_caption("Eunji's Rocket Game")

	# Make a rocket.
	rock = Rock(rk_settings, screen)
	
	# Make a star
	star = Star(rk_settings, screen)
	
	# Make a group to store bullets in.
	bullets = Group()
	stars = Group()
	
	# Create the fleet of aliens.
	gf.create_fleet(rk_settings, screen, rock, stars)
	
	# Start the main loop for the game.
	while True:
		
		# Watch for keyboard and mouse events.
		gf.check_events(rk_settings, screen, rock, bullets)
		rock.update()
		gf.update_bullets(bullets)
		gf.update_screen(rk_settings, screen, rock, stars, bullets)
		
		
	

run_game()

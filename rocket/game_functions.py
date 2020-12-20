import sys
import pygame
from bullet import Bullet
from star import Star


def check_events(rk_settings, screen, rock, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, rk_settings, screen, rock, bullets)
				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, rock)
				
def check_keydown_events(event, rk_settings, screen, rock, bullets):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		rock.moving_right = True
			
	elif event.key == pygame.K_LEFT:
		rock.moving_left = True
			
	elif event.key == pygame.K_UP:
		rock.moving_up = True
			
	elif event.key == pygame.K_DOWN:
		rock.moving_down = True
	
	elif event.key == pygame.K_SPACE:
		fire_bullet(rk_settings, screen, rock, bullets)
		
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, rock):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		rock.moving_right = False
				
	elif event.key == pygame.K_LEFT:
		rock.moving_left = False
	
	elif event.key == pygame.K_UP:
		rock.moving_up = False
				
	elif event.key == pygame.K_DOWN:
		rock.moving_down = False

def update_screen(rk_settings, screen, rock, stars, bullets):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(rk_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	rock.blitme()
	stars.draw(screen)
		
	# Make the most recently drawn screen visible.
	pygame.display.flip()

def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.right >= 1000:
			bullets.remove(bullet)
	

def fire_bullet(rk_settings, screen, rock, bullets):
	"""Fire a bullet if limit not reached yet."""
	if len(bullets) < rk_settings.bullets_allowed:
			new_bullet = Bullet(rk_settings, screen, rock)
			bullets.add(new_bullet)

def get_number_stars_x(rk_settings, star_width):
	"""Determine the number of stars that fit in a row."""
	available_space_x = rk_settings.screen_width - 2 * star_width
	number_stars_x = int(available_space_x / (2 * star_width))
	return number_stars_x

def create_star(rk_settings, screen, stars, star_number, row_number):
	"""Create an alien and place it in the row."""
	star = Star(rk_settings, screen)
	star_width = star.rect.width
	star.x = star_width + 2 * star_width * star_number
	star.rect.x = star.x
	star.rect.y = star.rect.height + 2 * star.rect.height * row_number
	stars.add(star)
	
	
def get_number_rows(rk_settings, rock_height, star_height):
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (rk_settings.screen_height -
						(3 * star_height) - rock_height)
	number_rows = int(available_space_y / (2 * star_height))
	return number_rows

def create_fleet(rk_settings, screen, rock, stars):
	"""Create a full fleet of stars."""
	# Create a star and find the number of stars in a row.
	star = Star(rk_settings, screen)
	number_stars_x = get_number_stars_x(rk_settings, star.rect.width)
	number_rows = get_number_rows(rk_settings, rock.rect.height, 
									star.rect.height)
									
	# Create the first row of stars.
	for row_number in range(number_rows):
		for star_number in range(number_stars_x):
			create_star(rk_settings, screen, stars, star_number,
						row_number)
		

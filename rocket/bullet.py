import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, rk_settings, screen, rock):
		super(Bullet, self).__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0, 0, rk_settings.bullet_width,
		rk_settings.bullet_height)
		self.rect.centerx = rock.rect.centerx
		self.rect.top = rock.rect.top
		
		self.x = float(self.rect.x)
		
		self.color = rk_settings.bullet_color
		self.speed_factor = rk_settings.bullet_speed_factor

	def update(self):
		self.x += self.speed_factor
		self.rect.x = self.x
	
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

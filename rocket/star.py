import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A clas to represent a single star in the fleet."""
	
	def __init__(self, rk_settings, screen):
		"""Initialize the star and set its starting position."""
		super(Star, self).__init__()
		self.screen = screen
		self.rk_settings = rk_settings
		
		# Load the star image and set its rect attribute.
		self.image = pygame.image.load('images/star.png')
		self.rect = self.image.get_rect()
		
		# Start each new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# Store the star's exact position.
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""Draw the star at its current locaiton."""
		self.screen.blit(self.image, self.rect)

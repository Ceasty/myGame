import pygame

class Ship:

	def __init__(self, info_world_game):
		self.screen = info_world_game.screen
		self.screen_rect = info_world_game.screen.get_rect()

		self.image = pygame.image.load('img/ship.PNG')
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

	def blit_ship(self):
		#update frame dalam game every location
		self.screen.blit(self.image, self.rect)
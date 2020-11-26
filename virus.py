import pygame
from pygame.sprite import Sprite

class Virus(Sprite):

	def __init__(self, AlienWorld):

		super().__init__()
		self.screen = AlienWorld.screen

		self.image = pygame.image.load('img/virus2.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
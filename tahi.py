import pygame
from pygame.sprite import Sprite

class Tahi(Sprite):

	def __init__(self, AlienWorld):

		super().__init__()
		self.screen = AlienWorld.screen
		self.settings = AlienWorld.my_settings

		#self.life = self.settings.tahi_life

		self.image = pygame.image.load('img/tahi.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)


	def update(self):
		self.x += (self.settings.tahi_speed * self.settings.tahi_direction)
		self.rect.x = self.x


	def check_edges(self):
		#screen_rect = self.screen.get_rect() #bentuk list ambil ukuran screen game #ga perlu lagi karena data langsung tarik dari settings
		if self.rect.right >= self.settings.window_width or self.rect.left <= 0:
			return True
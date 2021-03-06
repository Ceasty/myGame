import pygame
from pygame.sprite import Sprite 
#sprite adalah class yang telah dibuat oleh pygame

class Bullet(Sprite):

	def __init__(self, AlienWorld):
		super().__init__()#akses semua syntag
		#AlienWorld = semua info yang ada pada init utama di main
		self.settings = AlienWorld.my_settings
		self.screen = AlienWorld.screen

		self.color = self.settings.bullet_color


		self.rect = pygame.Rect(0,0, self. settings.bullet_width, self.settings.bullet_height)

		self.rect.midtop = AlienWorld.my_toilet.rect.midtop

		self.y = float(self.rect.y)


	def update(self):
		self.y -= self.settings.bullet_speed

		self.rect.y = self.y

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
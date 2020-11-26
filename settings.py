import sys
import pygame

class Settings:

	def __init__(self):
		self.window_width = 850
		self.window_height = 600
		self.bg_color = pygame.image.load('img/walls.png')
		self.screen = pygame.display.set_mode([self.window_width, self.window_height])
		self.my_screen = self.screen.get_rect()

		#ship
		self.toilet_speed = 3
		self.toilet_life = 1

		#bullet
		self.bullet_ammo = 18
		self.bullet_speed = 3.0
		self.bullet_width = 850
		self.bullet_height = 10
		self.bullet_color = (60, 242, 19)



		#tahi settings:
		#xself.tahi_life = 1
		self.tahi_speed = 2
		self.tahi_drop_speed = 30
		self.tahi_direction = 1 # 1 = ke kanan -1 = ke kiri



	def blit_back(self):
		self.screen.blit(self.bg_color , [-600,-800])
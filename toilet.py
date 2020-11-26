import pygame

class Toilet:

	def __init__(self, AlienWorld):
		self.screen = AlienWorld.screen
		self.screen_rect = AlienWorld.screen.get_rect()

		self.settings = AlienWorld.my_settings

		self.image = pygame.image.load("img/toilet2.png")
		self.rect = self.image.get_rect()

		self.re_position_toilet()

		#Status Movement
		self.moving_up = False
		self.moving_down = False
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_up and self.rect.top > 0 : #atau self.rect.top:
			#self.rect.y -=5
			self.y -= self.settings.toilet_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
			#self.rect.y +=5
			self.y += self.settings.toilet_speed
		if self.moving_right and self.rect.right < self.screen_rect.right :
			#self.rect.x +=5
			self.x += self.settings.toilet_speed
		if self.moving_left and self.rect.left > 0 : #atau self.rect.left :
			#self.rect.x -=5
			self.x -= self.settings.toilet_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def re_position_toilet(self):
		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blit_toilet(self):
		#update frame dalam game every location
		self.screen.blit(self.image, self.rect)
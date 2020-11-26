import pygame
import sys
import random
from time import sleep

from tahi import Tahi
from settings import Settings
from toilet import Toilet
from bullet import Bullet
from virus import Virus
from game_stat import GameStats

class AlienWorld:

	def __init__(self):
		pygame.init()
		self.my_settings = Settings()

		self.error = False
		self.screen = pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])
		#self.screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)

		self.title = pygame.display.set_caption("Game Toilet")
		self.bg_color = self.my_settings.bg_color


		
		self.bullets = pygame.sprite.Group() #container for bullet, tujuan biar ketika remove bullet semua bullet tidak hilang/
		self.my_toilet = Toilet(self)
		self.tahi_army = pygame.sprite.Group() #container for tai.
		self.my_viruses = pygame.sprite.Group()

		self.my_stats = GameStats(self)

		self.create_tahi_army()
		self.create_my_viruses()

	def run_game(self):
		while not self.error:
			self.check_events() #refactoring
			self.update_toilet()
			self.update_bullet()
			self.update_tahi()



			self.update_frame() #refactoring

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#sys.exit()
				self.error = True
			#elif event.type == pygame.KEYUP:
				#if event.key == pygame.K_q:
					#self.error = True

			elif event.type == pygame.KEYDOWN:
				self.check_keydown_event(event) #refactoring

			elif event.type == pygame.KEYUP:
				self.check_keyup_event(event) #refactoring





	def check_keydown_event(self, event):
		if event.key == pygame.K_w: 
			self.my_toilet.moving_up = True
		elif event.key == pygame.K_s: 
			self.my_toilet.moving_down = True
		elif event.key == pygame.K_d:
			self.my_toilet.moving_right = True
		elif event.key == pygame.K_a:
			self.my_toilet.moving_left = True
		elif event.key == pygame.K_SPACE: #fire!
			self.fire_bullet()
		elif event.key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_RCTRL:
			self.screen == pygame.display.set_mode([0,0], pygame.FULLSCREEN)
		elif event.key == pygame.K_f and pygame.key.get_mods() & pygame.KMOD_SHIFT:
			self.screen == pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])


	def check_keyup_event(self, event):
		if event.key == pygame.K_w:
			self.my_toilet.moving_up = False
		elif event.key == pygame.K_s:
			self.my_toilet.moving_down = False
		elif event.key == pygame.K_d:
			self.my_toilet.moving_right = False
		elif event.key == pygame.K_a:
			self.my_toilet.moving_left = False
		elif event.key == pygame.K_q:
			self.error = True

	def fire_bullet(self):
		if len(self.bullets) < self.my_settings.bullet_ammo :#len membaca jumlah #itu ekstra settings utk baca ammo dari settin.
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def update_toilet(self):
		self.my_toilet.update()

		if pygame.sprite.spritecollideany(self.my_toilet, self.tahi_army):
			#print('Kapal Menabrak Kecoa')
			self.toilet_hit()

	def toilet_hit(self):
		self.my_stats.toilet_life -= 1

		self.tahi_army.empty()
		self.bullets.empty()

		self.create_tahi_army()
		self.my_toilet.re_position_toilet() #set ulang posisi ship(toilet)

		sleep(0.1)

	def update_bullet(self): #awalnya remove bullet
		self.bullets.update()#dipindahkan

		for bullet in self.bullets.copy(): # copy() utk membuat salinan tanpa hapus yang asli
			if bullet.rect.bottom <= 0: #diambil bottom biar peluru ketika sampai diujung hilang jika top baru top sentuh border sudah hilang.
				self.bullets.remove(bullet)

		self.check_bullet_tahi_collision()


	def check_bullet_tahi_collision(self):

		collisions = pygame.sprite.groupcollide(self.bullets, self.tahi_army, True, True) #collision 2 benda
		'''
		collisions = pygame.sprite.groupcollide(self.tahi_army, self.bullets, False, True)
		for hit_tahi in collisions:
			hit_tahi.life -= 1

			if hit_tahi.life == 0:
				self.tahi_army.remove(hit_tahi)
		'''

		#print(len(self.bullets))#liat jum peluru

		if len(self.tahi_army) == 0:
			self.bullets.empty()
			self.create_tahi_army()



	def create_tahi(self, each_tahi, each_row):
			tahi = Tahi(self)
			#tahi_width, tahi_height = tahi.rect.size
			#atau boleh
			tahi_width = tahi.rect.width
			tahi_height = tahi.rect.height

			tahi.x = tahi_width + (2 * tahi_width * each_tahi)
			tahi.y = tahi_height + (2* tahi_height * each_row) # hitung jumlah row yang mungkin.
			tahi.rect.x = tahi.x
			tahi.rect.y = tahi.y
			self.tahi_army.add(tahi)#masukin 
		
	def create_tahi_army(self):#membuat tai bergeser ke kanan
		tahi = Tahi(self)
		#tahi_width, tahi_height = tahi.rect.size
		#atau boleh
		tahi_width = tahi.rect.width
		tahi_height = tahi.rect.height		
		avaiable_space_for_tahi = self.my_settings.window_width - (2 * tahi_width) #hitung space yang dimiliki
		number_of_tahi = avaiable_space_for_tahi // (2*tahi_width) #jumlah tahi yang muat di urutan

		ship_p1_height = self.my_toilet.rect.height
		avaiable_space_for_row = self.my_settings.window_height - (2 * tahi_height) - (ship_p1_height)
		number_of_row = avaiable_space_for_tahi // (3*tahi_height) #hitung jumlah row yang mungkin.

		for each_row in range(number_of_row): # mengkalikan setiap row
			for each_tahi in range(number_of_tahi + 1): # mengkalikan jumllah tahi muat berapa column.
				self.create_tahi(each_tahi, each_row)


	def update_tahi(self):
		self.tahi_army.update()
		self.check_tahi_army()

	def check_tahi_army(self):
		for tahi in self.tahi_army.sprites():
			if tahi.check_edges():
				self.change_direction_tahi_army()
				break#biar stop ga berulang

	def change_direction_tahi_army(self):
		for tahi in self.tahi_army.sprites():
			tahi.rect.y += self.my_settings.tahi_drop_speed
		self.my_settings.tahi_direction *= -1


	def create_virus(self,pos_x,pos_y):
		virus = Virus(self)
		virus.rect.x, virus.rect.y = pos_x, pos_y
		self.my_viruses.add(virus)

	def create_my_viruses(self):
		virus = Virus(self)
		virus_width, virus_height = virus.rect.size
		number_of_viruses = (self.my_settings.window_width * self.my_settings.window_height)//(virus_width*virus_height)
		#utk menentukan jumlah maksimal. dari star yang muat di window.
		for each_virus in range (number_of_viruses//5):
			pos_x = random.randint(0,self.my_settings.window_width)
			pos_y = random.randint(0,self.my_settings.window_height)
			self.create_virus(pos_x, pos_y)


	def blit_backround(self):
		self.screen.blit(self.my_settings.bg_color , [-300,-130])#frame for backround.
		#wokeh


	def update_frame(self):
		self.blit_backround()#backround blit.
		self.my_viruses.draw(self.screen)#spawn Virus
		self.my_toilet.blit_toilet()

		for bullet in self.bullets.sprites():
			bullet.draw()

		self.tahi_army.draw(self.screen)

		pygame.display.flip()


Game_ALIEN = AlienWorld()
Game_ALIEN.run_game()

class GameStats:
	def __init__(self, Alienworld):
		self.setting = Alienworld.my_settings
		self.reset_stats()

	def reset_stats(self):
		self.toilet_life = self.setting.toilet_life

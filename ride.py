
class Ride:
	def __init__ (self, idx, tuple):
		self.idx = idx

		self.start = tuple[0], tuple[1]
		self.stop = tuple[2], tuple[3]
		self.start_time = tuple[-2]
		self.stop_time = tuple[-1]
		
		self.duration = abs(self.stop[0] - self.start[0]) + abs(self.stop[1] - self.start[1])
		self.last_call = self.stop_time - self.duration


	def get_dispos (self, cars):
		dispos = []

		for car in cars:
			if car[3] + abs(car[0] - self.start[0]) + abs(car[1] - self.start[1]) <= self.last_call:
				dispos.append(car)

		return dispos


	def get_nearest (self, cars):
		nearest = -1
		min_dist = 1000000

		for car in cars:
			dist = car[3] + abs(car[0] - self.start[0]) + abs(car[1] - self.start[1])
			
			if dist <= min_dist:
				min_dist = dist
				nearest = car[0]

		return nearest





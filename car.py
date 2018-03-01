
class Car:
	def __init__ (self, idx):
		self.idx = idx

		self.x = 0
		self.y = 0
		self.t = 0

	def get_nearest_ride (self, rides, max_time):
		min_time = 1000000
		min_ride = -1
		min_idx = -1

		for list_idx, ride in enumerate(rides):
			if self.t + self.dist(ride) > ride.last_call:
				continue

			time = max(ride.start_time, self.t + self.dist(ride))

			if time > max_time:
				continue
			
			if time < min_time:
				min_time = time
				min_ride = ride
				min_idx = list_idx

		return min_time, min_ride, min_idx


	def dist (self, ride):
		return abs(self.x - ride.start[0]) + abs(self.y - ride.start[1])

			
			


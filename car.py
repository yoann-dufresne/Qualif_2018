
class Car:
	def __init__ (self, idx):
		self.idx = idx

		self.x = 0
		self.y = 0
		self.t = 0

	def get_nearest_ride (self, rides, max_time, bonus):
		min_time = 1000000
		min_modified_time = 1000000
		min_ride = -1
		min_idx = -1

		for list_idx, ride in enumerate(rides):
			if self.t + self.dist(ride) > ride.last_call:
				continue

			start_time = max(ride.start_time, self.t + self.dist(ride))

			if start_time + ride.duration > max_time:
				continue

			modified_time = start_time - bonus if start_time == ride.start_time else start_time
			
			if modified_time < min_modified_time:
				min_time = start_time
				min_ride = ride
				min_idx = list_idx
				min_modified_time = modified_time

		return min_time, min_ride, min_idx


	def dist (self, ride):
		return abs(self.x - ride.start[0]) + abs(self.y - ride.start[1])

			
			


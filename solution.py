

class Solution:

	def __init__ (self, nb_cars):
		self.cars = [[] for _ in range(nb_cars)]


	def to_string(self):
		string = ""

		for car in self.cars:
			string += "{} {}\n".format(len(car), " ".join(map(str, car)))

		return string


	def score(self, problem):
		nb_rows, nb_cols, nb_cars, nb_rides, bonus, steps, rides = problem
		car_state = dict()
		points = 0
		for car_idx in range(len(self.cars)):
			time = 0
			previous_x, previous_y = 0, 0
			for ride_idx in self.cars[car_idx]:
				ride = [ride for ride in rides if ride.idx == ride_idx][0] # slow but works
				assert(ride_idx == ride.idx)
				start, stop = ride.start, ride.stop
				earliest_time = ride.start_time
				latest_time = ride.stop_time
				time += abs(start[0] - previous_x) + abs(start[1] - previous_y) # advance time to go to next pick up
				extra_points = 0
				if time <= earliest_time :
					extra_points = bonus
					time = earliest_time # avance le temps d'au moins le temps de course
				#print("car %d, ride %d is now at time %d " % (car_idx, ride_idx, time))	
				distance = abs(stop[1]-start[1]) + abs(stop[0]-start[0])
				previous_x, previous_y = stop
				time += distance
				if time > latest_time:
					print("warning: car %d, ride %d at time %d is too late (should be between times %d and %d)" % (car_idx, ride_idx, time, earliest_time, latest_time))	
				else:
					points += distance + extra_points
				
		return points

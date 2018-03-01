from solution import Solution
from operator import itemgetter
from copy import deepcopy

from ride import Ride
from car import Car


def solve (problem):
	cars = [Car(idx) for idx in range(problem[2])]
	sol = Solution(problem[2])

	rides = problem[6]
	# Sort by dates
	# rides.sort(key=lambda r: (r.start_time, r.stop_time))

	for car in cars:
		while True:
			min_time, ride, idx = car.get_nearest_ride(rides, problem[5])

			if ride == -1:
				break

			# Add ride idx to sol
			sol.cars[car.idx].append(ride.idx)

			# remove ride from list
			rides.pop(idx)

			# update car
			car.x = ride.stop[0]
			car.y = ride.stop[1]
			car.t = min_time + car.dist(ride)


	return sol



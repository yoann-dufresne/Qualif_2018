from solution import Solution
from operator import itemgetter
from copy import deepcopy

from ride import Ride


def solve (problem):
	cars = [(idx, 0, 0, 0) for idx in range(problem[2])]
	sol = Solution(problem[2])

	rides = problem[6]
	# Sort by dates
	rides.sort(key=lambda r: (r.start_time, r.stop_time))

	for ride in rides:
		# Get dispos
		dispos = ride.get_dispos(deepcopy(cars))

		# Get nearest car
		nearest = ride.get_nearest(dispos)

		# attribute ride to car
		if nearest != -1:
			sol.cars[nearest].append(ride.idx)
			cars[nearest] = (nearest, ride.stop[0], ride.stop[1], max(cars[nearest][-1], ride.start_time) + ride.duration)


	return sol



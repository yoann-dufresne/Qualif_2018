from solution import Solution
from operator import itemgetter

from ride import Ride


def solve (problem):
	cars = [(idx, 0, 0, 0) for idx in range(problem[2])]

	rides = problem[6]
	# Sort by dates
	rides.sort(key=lambda r: (r.start_time, r.stop_time))

	for ride in rides:
		# Get dispos
		dispos = ride.get_dispos(cars)

		# 
		print(dispos)

	return Solution(problem[2])



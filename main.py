#!/usr/bin/env python3

import sys
import argparse

from ride import Ride
from solution import Solution
from naive import solve
import os.path


def main ():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("filename", help="File containing the problem")
	# arg_parser.add_argument("-sol", help="Load a pre-solution")
	args = arg_parser.parse_args()

	name = args.filename.split("/")[-1].split('.')[0]

	problem = parse_problem (args.filename)
	sol = solve(problem)
	print(sol.to_string())

	return 0


def parse_problem (filename):
	with open(filename, "r") as file:
		header = file.readline().strip()
		nb_rows, nb_cols, nb_cars, nb_rides, bonus, steps = [int(x) for x in header.split()]

		rides = []
		for ride_idx in range(nb_rides):
			rides.append(Ride(ride_idx, tuple([*[int(x) for x in file.readline().strip().split()]])))

	return nb_rows, nb_cols, nb_cars, nb_rides, bonus, steps, rides


if __name__ == "__main__":
	main()

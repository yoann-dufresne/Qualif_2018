#!/usr/bin/env python3

import sys
import argparse

import slices
from solution import Solution
import solver_random
import solver_hill_climbing as solver

import os.path


def main ():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("filename", help="File containing the problem")
	# arg_parser.add_argument("-sol", help="Load a pre-solution")
	args = arg_parser.parse_args()

	name = args.filename.split("/")[-1].split('.')[0]

	toto = parse_problem (args.filename)
	sol = Solution(pizza)

	return 0


def parse_problem (filename):
	with open(filename, "r") as file:
		header = file.readline().strip()
		nb_rows, nb_cols, min_mushrooms, max_size = [int(x) for x in header.split()]

		pizza = []
		for i in range(nb_rows):
			row = file.readline().strip()
			pizza.append([True if x=='M' else False for x in row])

	return pizza, (max_size, min_mushrooms)


if __name__ == "__main__":
	main()

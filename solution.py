

class Solution:

	def __init__ (self, nb_cars):
		self.cars = [[] for _ in range(nb_cars)]


	def to_string(self):
		string = ""

		for car in self.cars:
			string += "{} {}\n".format(len(car), " ".join(map(str, car)))

		return string

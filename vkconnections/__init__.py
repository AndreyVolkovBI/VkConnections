from vkconnections.vkconnections import main as m
import sys

class Create:
	# keys - list of given keys
	def __init__(self, keys):
		if len(keys) != 4:
			sys.exit("List of keys should have 4 different keys.")
		self.keys = keys
		
	def getConnection(self, userFrom, userTo):
		return m.getWayBetween(userFrom, userTo, self.keys)

	def printConnection(result, photo=False):
		for way in temp:
			for person in way:
				s = "Id: " + str(person['id']) + " " + "Name: " + person['full_name']
				s += "Photo: " + person['photo'] if photo else ""
				print(s)
			print()
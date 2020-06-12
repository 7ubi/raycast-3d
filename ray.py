import pygame
from wall import Wall
import math

class Ray:
	def __init__(self, x, y, angle):
		self.x = x
		self.y = y
		self.dirX = math.cos(angle)
		self.dirY = math.sin(angle)

	def cast(self, wall):
		x1 = wall.x1
		x2 = wall.x2
		y1 = wall.y1
		y2 = wall.y2

		x3 = self.x
		x4 = self.x + self.dirX
		y3 = self.y
		y4 = self.y + self.dirY

		den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

		if den == 0:
			return -100, -100

		t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
		u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

		if t > 0 and t < 1 and u > 0:
			x5 = x1 + t * (x2 - x1)
			y5 = y1 + t * (y2 - y1)
			return x5, y5
		return -100, -100

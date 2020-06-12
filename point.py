import pygame
from ray import Ray
from wall import Wall
import numpy as np
import math

def dist(x1, y1, x2, y2):
	return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

def map(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = float(value - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)

class Point:
	def __init__(self, pos, n, fov, w, h):
		self.x, self.y = pos
		self.rays = []
		self.speed = 1
		self.angle = 0
		self.n = n
		self.fov = fov
		self.w = w / n
		self.maxh1 = dist(0, 0, w, h)
		self.maxh2 = h

		for i in range(n):
			self.rays.append(Ray(self.x, self.y, -(np.pi / 4) + self.angle + (i * 2 * np.pi / (n * fov))))
		
	def move(self, dir):
		self.x += dir * self.speed * math.cos(self.angle)
		self.y += dir * self.speed * math.sin(self.angle)
		
		for ray in self.rays:
			ray.x = int(self.x)
			ray.y = int(self.y)

	def rotate(self, phi):
		self.rays = []
		self.angle += phi
		self.angle = self.angle % (np.pi * 2)

		for i in range(self.n):
			self.rays.append(Ray(int(self.x), int(self.y), -(np.pi / 4) + self.angle + (i * 2 * np.pi / (self.n * self.fov))))


	def look(self, walls, screen):
		for i in range(len(self.rays)):
			ray = self.rays[i]
			clostest = None
			record = np.Inf

			for wall in walls:
				x1, y1 = ray.cast(wall)
				if x1 == -100 and y1 == -100:
					continue
				d = dist(x1, y1, self.x, self.y)

				if d < record:
					clostest = (x1, y1)
					record = d
			if clostest != None:
				x, y = clostest
				d = dist(x, y, self.x, self.y)

				h = map(d, 0, self.maxh1, self.maxh2, 0)
				pygame.draw.rect(screen, pygame.Color(255, 255, 255), (i * int(self.w) + self.n * self.w, self.maxh2/2 - h / 2, int(self.w), h))
				pygame.draw.line(screen, pygame.Color(255, 255, 255), (ray.x + self.w, ray.y), clostest)


	def draw(self, screen):
		pygame.draw.circle(screen, pygame.Color(255, 255, 255), (int(self.x), int(self.y)), 3)
import pygame

class Wall:
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

	

	def draw(self, screen):
		pygame.draw.line(screen, pygame.Color(255, 255, 255), (self.x1, self.y1), (self.x2, self.y2))
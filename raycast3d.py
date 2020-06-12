import pygame
import sys
from wall import Wall
from point import Point

pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RAYCAST 3D")

clock = pygame.time.Clock()


walls = [Wall(200, 200, 100, 300), Wall(100, 500, 200, 400)] #Wall(400, 100, 200, 300), Wall(0, 0, 0, height), Wall(0, height, width, height), Wall(0, 0, width, 0), Wall(width, 0, width, height)]
p = Point((250, 250), 100, 4, width / 2, height)

def main():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		screen.fill(pygame.Color(0, 0, 0))

		for wall in walls:
			wall.draw(screen)

		key = pygame.key.get_pressed()

		if key[pygame.K_w]:
			p.move(1)

		if key[pygame.K_s]:
			p.move(-1)

		if key[pygame.K_d]:
			p.rotate(0.1)

		if key[pygame.K_a]:
			p.rotate(-0.1)

		p.draw(screen)
		p.look(walls, screen)
		pygame.display.update()
		clock.tick(30)

		


main()
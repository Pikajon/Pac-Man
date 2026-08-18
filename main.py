import pygame
pygame.init()
height = 600
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac Man")
black = pygame.Color(0,0,0)
running = True

while running:
	screen.fill(black)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()

pygame.quit()


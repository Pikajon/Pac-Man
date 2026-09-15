import pygame
from player import Player
pygame.init()
height = 600
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac Man")
darkblue = pygame.Color(0,0,139)
running = True
clock = pygame.time.Clock()
black_color = [0,0,0]
food = pygame.transform.scale(pygame.image.load("food.png"), (10,10))
player = Player()

#wall = 0
#dot = 1
#empty = 2

def draw_grid(screen):
	for i in range(12):

		for j in range(16):
			if map_grid[i][j] == 0:
				pygame.draw.rect(screen,black_color,(j*50,i*50,50,50))
			if map_grid[i][j] == 1:
				screen.blit(food,(j*50+20,i*50+20))

map_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
    [2, 1, 1, 1, 1, 1, 0, 2, 2, 0, 1, 1, 1, 1, 1, 2],
    [0, 1, 0, 0, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 1, 1, 0],
    [2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2],
    [0, 1, 0, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]




while running:
	screen.fill(darkblue)
	player.draw(screen)
	player.move()
	player.move_pacman()
	draw_grid(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			player.handle_input(event.key)

	pygame.display.update()
	clock.tick(10)
pygame.quit()


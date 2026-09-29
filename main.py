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
    [3, 1, 1, 1, 1, 1, 0, 2, 2, 0, 1, 1, 1, 1, 1, 3],
    [0, 1, 0, 0, 0, 1, 0, 2, 2, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 1, 1, 0],
    [3, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 3],
    [0, 1, 0, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def collision_check(x,y, x_change, y_change):
	next_x = x + x_change
	next_y = y + y_change

	if x_change > 0: next_x += 49
	if y_change > 0: next_y += 49

	i = int(next_y // 50)
	j = int(next_x // 50)

	if 0 <= i < 12 and 0 <= j < 16:
		return map_grid[i][j] == 0
	return False

def eat_food(x, y):
	if x % 50 == 0 and y % 50 == 0:
		i = int(y / 50)
		j = int(x / 50)
		if map_grid[i][j] == 1:
			map_grid[i][j] = 2

def pass_wall(x, y):
	if x == 0 and y == 200:
		player.x = 800
	elif x == 0 and y == 350:
		player.x = 800
	elif x == 750 and y == 200:
		player.x = 0
	elif x == 750 and y == 350:
		player.x = 0



while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			player.handle_input(event.key)

	if collision_check(player.x,player.y,player.x_change,player.y_change):
		player.x_change = 0
		player.y_change = 0
	if player.x % 50 == 0 and player.y % 50 == 0:
		if collision_check(player.x,player.y,player.next_x_change,player.next_y_change):
			player.next_x_change = 0
			player.next_y_change = 0

	pass_wall(player.x,player.y)
	screen.fill(darkblue)
	player.draw(screen)
	player.move()
	player.move_pacman()
	draw_grid(screen)
	eat_food(player.x,player.y)

	pygame.display.update()
	clock.tick(45)
pygame.quit()



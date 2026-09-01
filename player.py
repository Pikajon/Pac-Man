import pygame
class Player:
	def __init__(self):
		self.size = None
		self.y = 250
		self.x = 350
		self.speed = None
		self.image = pygame.transform.scale(pygame.image.load("pacman.png"), (50,50))
		self.x_change = 0
		self.y_change = 0

	def draw(self, screen):
		screen.blit(self.image,(self.x, self.y))

	def handle_input(self, key):
		if key == pygame.K_LEFT:
			self.x_change = -3
			self.y_change = 0
			self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("pacman.png"), (50, 50)), True, False)
		if key == pygame.K_RIGHT:
			self.x_change = 3
			self.y_change = 0
			self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pacman.png"), (50, 50)), 360)
		if key == pygame.K_UP:
			self.y_change = -3
			self.x_change = 0
			self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pacman.png"), (50, 50)), 90)
		if key == pygame.K_DOWN:
			self.y_change = 3
			self.x_change = 0
			self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pacman.png"), (50, 50)), 270)

	def move(self):
		self.x += self.x_change
		self.y += self.y_change




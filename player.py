import pygame
class Player:
	def __init__(self):
		self.size = None
		self.y = 400
		self.x = 350
		self.speed = None
		self.image = pygame.transform.scale(pygame.image.load("pacman.png"), (50,50))
		self.x_change = 0
		self.y_change = 0
		self.next_y_change = 0
		self.next_x_change = 0
		self.move_pending = 0
		self.next_x = 0
		self.next_y = 0

	def draw(self, screen):
		screen.blit(self.image,(self.x, self.y))

	def handle_input(self, key):
		if key == pygame.K_LEFT:
			self.next_x_change = -5
			self.next_y_change = 0
			self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("pacman.png"), (50,50)), True, False)
		if key == pygame.K_RIGHT:
			self.next_x_change = 5
			self.next_y_change = 0
			self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pacman.png"), (50,50)), 360)
		if key == pygame.K_UP:
			self.next_y_change = -5
			self.next_x_change = 0
			self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pacman.png"), (50,50)), 90)
		if key == pygame.K_DOWN:
			self.next_y_change = 5
			self.next_x_change = 0
			self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pacman.png"), (50, 50)), 270)

	def move(self):
		if self.x % 50 == 0 and self.y % 50 == 0:
			self.x_change = self.next_x_change
			self.y_change = self.next_y_change

		self.x += self.x_change
		self.y += self.y_change
		self.next_x = self.x + self.next_x_change
		self.next_y = self.y + self.next_y_change
		if self.move_pending > 0:
			self.move_pending -= 1

	def move_pacman(self):
		self.move_pending += 10






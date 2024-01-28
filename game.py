import pygame

class game():
	def __init__(self):
		self.PygameSetup()

	def PygameSetup(self):
		pygame.init()
		self.DISPLAYSURF = pygame.display.set_mode((400,300))
		pygame.display.set_caption('X-Wing')

class mover():
	pass

class Gui():
	pass
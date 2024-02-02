import pygame

class game():
	def __init__(self):
		self.PygameSetup()
		self.GameLoop()
		

	def PygameSetup(self):
		pygame.init()
		self.DISPLAYSURF = pygame.display.set_mode((400,300))
		pygame.display.set_caption('X-Wing')

	def GameLoop(self):
		#loop
		while True:
			for event in pygame.event.get():
				if event.type == 'QUIT':
					pygame.quit()
					sys.exit()
					pygame.display.update()

	def screenshot(self):
		pygame.image.save(self.DISPLAYSURF, "shots/screenshot.jpg")

class mover():
	pass

class Gui():
	pass
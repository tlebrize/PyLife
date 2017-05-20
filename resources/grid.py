from .cell import PLCell

class PLGrid(object):

	def __init__(self):
		self.size = 15
		self.x = 0
		self.y = 0
		self.cells = []
		for x in range(1, self.size):
			self.cells.append([PLCell(x, y) for y in range(1, self.size)])
		for x, line in enumerate(self.cells):
			for y in range(0, self.size - 1):
				self.cells[x][y].neighbours = {
					"E": self.cells[(x + 1) % self.size - 1][y],
					"W": self.cells[(x - 1) % self.size - 1][y],
					"S": self.cells[x][(y - 1) % self.size - 1],
					"N": self.cells[x][(y + 1) % self.size - 1],
					"NE": self.cells[(x + 1) % self.size - 1][(y + 1) % self.size - 1],
					"NW": self.cells[(x - 1) % self.size - 1][(y + 1) % self.size - 1],
					"SE": self.cells[(x + 1) % self.size - 1][(y - 1) % self.size - 1],
					"SW": self.cells[(x - 1) % self.size - 1][(y - 1) % self.size - 1]
				}
		self.current = self.cells[self.x][self.y]
		self.current.selected = True

	def move_cursor(self, x, y):
		self.current.selected = False
		self.x = (self.x + x) % len(self.cells) 
		self.y = (self.y + y) % len(self.cells) 
		self.current = self.cells[self.x][self.y]
		self.current.selected = True

	def draw(self):
		for line in self.cells:
			for cell in line:
				cell.draw()

	def toggle(self):
		self.current.alive = not self.current.alive

	def update(self):
		for x, line in enumerate(self.cells):
			for y in range(0, self.size - 1):
				self.cells[x][y].update()
		for x, line in enumerate(self.cells):
			for y in range(0, self.size - 1):
				self.cells[x][y].alive = self.cells[x][y].alive_next
				self.cells[x][y].alive_next = False
					

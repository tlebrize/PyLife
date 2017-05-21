from .cell import PLCell

class PLGrid(object):

	def __init__(self, size, scale):
		self.size = size
		self.scale = scale
		self.redraw()

	def redraw(self):
		self.x = self.size // 2
		self.y = self.size // 2
		self.cells = []
		for x in range(1, self.size + 1):
			self.cells.append([PLCell(x, y, self.scale) for y in range(1, self.size + 1)])
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].neighbours = {
					"E": self.cells[(x - 1) % self.size][y],
					"W": self.cells[(x + 1) % self.size][y],
					"S": self.cells[x][(y - 1) % self.size],
					"N": self.cells[x][(y + 1) % self.size],
					"NE": self.cells[(x - 1) % self.size][(y + 1) % self.size],
					"NW": self.cells[(x + 1) % self.size][(y + 1) % self.size],
					"SE": self.cells[(x - 1) % self.size][(y - 1) % self.size],
					"SW": self.cells[(x + 1) % self.size][(y - 1) % self.size]
				}
		self.current = self.cells[self.x][self.y]
		self.current.selected = True

	def clear(self):
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].alive = False
				self.cells[x][y].alive_next = False

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
			for y in range(0, self.size):
				self.cells[x][y].update()
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].alive = self.cells[x][y].alive_next

from pyglet import gl

COLOR = {
	True: {True: (0.3, 0.3, 0.3), False: (0.7, 0.7, 0.7)},
	False: {True: (0.0, 0.0, 0.0), False: (1.0, 1.0, 1.0)}
}

class PLCell(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.selected = False
		self.alive = False
		self.alive_next = False
		self.neighbours = {}

	def draw(self):
		x, y = self.x, self.y
		color = COLOR[self.selected][self.alive]
		gl.glBegin(gl.GL_POLYGON)
		gl.glColor3f(*color)
		gl.glVertex2i((5 * x) + 50 * x - 25, (5 * y) + 50 * y - 25)
		gl.glVertex2i((5 * x) + 50 * x - 25, (5 * y) + 50 * y + 25)
		gl.glVertex2i((5 * x) + 50 * x + 25, (5 * y) + 50 * y + 25)
		gl.glVertex2i((5 * x) + 50 * x + 25, (5 * y) + 50 * y - 25)
		gl.glEnd()

	def update(self):
		count = sum([cell.alive for cell in self.neighbours.values()])
		if self.alive:
			if count < 2 or count > 3:
				self.alive_next = False
			else:
				self.alive_next = True
		else:
			if count == 3:
				self.alive_next = True
			else:
				self.alive_next = False

from pyglet import gl

class PLCell(object):
	
	COLOR = {
		True: {True: (0.3, 0.3, 0.3), False: (0.7, 0.7, 0.7)},
		False: {True: (0.0, 0.0, 0.0), False: (1.0, 1.0, 1.0)}
	}

	def __init__(self, x, y, s):
		self.selected = False
		self.alive = False
		self.alive_next = False
		self.neighbours = {}
		self.points = (
			((s * x) + s * 10 * x - s * 5, (s * y) + s * 10 * y - s * 5),
			((s * x) + s * 10 * x - s * 5, (s * y) + s * 10 * y + s * 5),
			((s * x) + s * 10 * x + s * 5, (s * y) + s * 10 * y + s * 5),
			((s * x) + s * 10 * x + s * 5, (s * y) + s * 10 * y - s * 5)
		)
		self.square = gl.glGenLists(1)
		gl.glNewList(self.square, gl.GL_COMPILE)
		self.draw_square()
		gl.glEndList()

	def draw_square(self):
		gl.glBegin(gl.GL_POLYGON)
		gl.glVertex2i(*self.points[0])
		gl.glVertex2i(*self.points[1])
		gl.glVertex2i(*self.points[2])
		gl.glVertex2i(*self.points[3])
		gl.glEnd()

	def draw(self):
		gl.glColor3f(*PLCell.COLOR[self.selected][self.alive])
		gl.glCallList(self.square)
		gl.glFlush()

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

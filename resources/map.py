import tkengine, pyglet
from pyglet import gl

class Cell(tkengine.TkPlainCell):

	COLOR = {
		True: {True: (0.3, 0.3, 0.3), False: (0.7, 0.7, 0.7)},
		False: {True: (0.0, 0.0, 0.0), False: (1.0, 1.0, 1.0)}
	}
	
	def __init__(self, x, y, scale):
		super(Cell, self).__init__(x, y, scale)
		self.alive = False
		self.alive_next = False

	def draw(self):
		self.color = Cell.COLOR[self.selected][self.alive]
		super(Cell, self).draw()

	def update(self):
		count = sum([cell.alive for cell in self.neighbors.values()])
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


class Map(tkengine.TkGridMap):

	SPEED = [1.0, 0.5, 0.3, 0.1, 0.05, 0.01]

	def __init__(self, world):
		self._init(world)
		self.running = False

	def _init(self, world=None):
		if world:
			self.world = world
		super(Map, self).__init__(self.world, Cell)
		self.key_handlers.update({
			pyglet.window.key.RETURN : self.toggle,
			pyglet.window.key.TAB : lambda: self.update(False),
			pyglet.window.key.SPACE : self.pause,
			pyglet.window.key.ESCAPE : self.quit
		})

	def clear(self):
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].alive = False
				self.cells[x][y].alive_next = False

	def toggle(self):
		self.current.alive = not self.current.alive

	def entry(self):
		self.running = False
		self.world.window.set_caption("PyLife - Paused")
		if self.world.scale != self.scale or self.world.size != self.size:
			self.scale = self.world.scale
			self.size = self.world.size
			self._init()
		self.world.window.set_size(
				self.world.scale * self.world.size * 11 + self.world.scale * 10,
				self.world.size * self.world.scale * 11 + self.world.scale * 10)
		self.world.window.center()
		pyglet.clock.schedule_interval(self.update, Map.SPEED[self.world.speed])
		pyglet.gl.glClearColor(0.42, 0.42, 0.42, 0)

	def pause(self):
		self.running = not self.running
		self.world.window.set_caption("PyLife - {}".format(
			"Running" if self.running else "Paused"))

	def quit(self):
		pyglet.clock.unschedule(self.update)
		self.running = False
		self.world.transition("main")

	def update(self, wait):
		if not self.running and wait:
			return
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].update()
		for x, line in enumerate(self.cells):
			for y in range(0, self.size):
				self.cells[x][y].alive = self.cells[x][y].alive_next



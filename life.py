import pyglet, collections
from resources.window	import TkWindow
from resources.world	import TkWorld
from resources.menu		import TkMenu
from resources.scene	import TkScene
from resources.option	import TkOption
from resources.grid		import PLGrid

class MainMenu(TkMenu):
	def __init__(self, world, label_y=200):
		self.label = "PyLife"
		self.menu_items = collections.OrderedDict((
			("Start"	, lambda: self.world.transition("life")),
			("Options"	, lambda: self.world.transition("options")),
			("Clear"	, lambda: self.world.scenes.get("life").grid.clear()),
			("Quit"		, lambda: self._quit())
		))
		super(MainMenu, self).__init__(world)

	def entry(self):
		self.world.window.set_caption("PyLife")
		pyglet.gl.glClearColor(0, 0, 0, 0)
		self.world.window.set_size(600, 600)
		self.world.window.center()

class LifeScene(TkScene):

	SPEED = [1.0, 0.5, 0.3, 0.1, 0.05, 0.01]

	def __init__(self, world):
		super(LifeScene, self).__init__(world)
		self.running = False
		self.grid = PLGrid(self.world.size, self.world.scale)
		self.key_handlers = {
			pyglet.window.key.RETURN : self.grid.toggle,
			pyglet.window.key.TAB : self.grid.update,
			pyglet.window.key.SPACE : self.pause,
			pyglet.window.key.ESCAPE : self.quit,
			pyglet.window.key.RIGHT : lambda : self.grid.move_cursor(1, 0),
 			pyglet.window.key.LEFT : lambda : self.grid.move_cursor(-1, 0),
			pyglet.window.key.DOWN : lambda : self.grid.move_cursor(0, -1),
			pyglet.window.key.UP : lambda : self.grid.move_cursor(0, 1),
		}
		pyglet.clock.schedule_interval(self.draw, 1 / 60)

	def update(self, _):
		if self.running:
			self.grid.update()

	def entry(self):
		self.running = False
		self.world.window.set_caption("PyLife - Paused")
		if self.world.scale != self.grid.scale or self.world.size != self.grid.size:
			self.grid.scale = self.world.scale
			self.grid.size = self.world.size
			self.grid.redraw()
		self.world.window.set_size(
				self.world.scale * self.world.size * 11 + self.world.scale * 10,
				self.world.size * self.world.scale * 11 + self.world.scale * 10)
		self.world.window.center()
		pyglet.clock.schedule_interval(self.update, LifeScene.SPEED[self.world.speed])
		pyglet.gl.glClearColor(0.42, 0.42, 0.42, 0)

	def pause(self):
		self.running = not self.running
		self.world.window.set_caption("PyLife - {}".format(
			"Running" if self.running else "Paused"))

	def quit(self):
		pyglet.clock.unschedule(self.update)
		self.running = False
		self.world.transition("main")

	def draw(self, _):
		self.world.window.clear()
		self.grid.draw()

class Options(TkOption):

	def __init__(self, world):
		world.set_options([
			["size", 25, 1, 100],
			["scale", 2, 1, 50],
			["speed", 3, 0, 5]
		])
		super(Options, self).__init__(world)

	def entry(self):
		self.world.window.set_caption("PyLife")


def main():
	window = TkWindow(600, 600, visible=False, caption="PyLife")
	world = TkWorld(window)
	main_menu = MainMenu(world)
	options = Options(world)
	life = LifeScene(world)
	world.add_scenes({"main": main_menu, "life": life, "options": options})
	world.transition("main")
	pyglet.app.run()

if __name__ == "__main__":
	main()
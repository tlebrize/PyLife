import pyglet
from resources.window	import TkWindow
from resources.world	import TkWorld
from resources.menu		import TkMenu
from resources.scene	import TkScene
from resources.grid		import PLGrid

class MainMenu(TkMenu):
	def __init__(self, world):
		self.label = "PyLife"
		self.menu_items = {
			"Start"		: self.start,
			"Quit"		: self.quit
		}
		super(MainMenu, self).__init__(world)

	def start(self):
		self.world.transition("life")

	def quit(self):
		self._quit()

class LifeScene(TkScene):
	
	def __init__(self, world):
		super(LifeScene, self).__init__(world)
		self.running = False
		self.grid = PLGrid()
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

	def update(self, _):
		if self.running:
			self.grid.update()

	def entry(self):
		self.running = False
		pyglet.gl.glClearColor(0.42, 0.42, 0.42, 0)

	def pause(self):
		self.running = not self.running
		self.world.window.set_caption("PyLife - {}".format(
			"Running" if self.running else "Paused"))

	def quit(self):
		self.running = False
		self.world.transition("main_menu")

	def on_key_press(self, button, modifiers):
		handler = self.key_handlers.get(button, lambda: None)
		handler()

	def on_draw(self):
		self.world.window.clear()
		self.grid.draw()

def main():
	window = TkWindow(825, 825, visible=False, caption="PyLife - Paused", style="dialog")
	world = TkWorld(window)
	main_menu = MainMenu(world)
	life = LifeScene(world)
	world.add_scenes({"main_menu": main_menu, "life": life})
	world.transition("main_menu")
	pyglet.clock.schedule_interval(life.update, 0.4)
	pyglet.app.run()

if __name__ == "__main__":
	main()
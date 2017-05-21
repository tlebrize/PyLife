import tkengine, collections, pyglet

class Menu(tkengine.TkMenu):
	def __init__(self, world):
		super(Menu, self).__init__(world, label="PyLife", menu_items=(
			("Start"	, lambda: self.world.transition("life")),
			("Options"	, lambda: self.world.transition("options")),
			("Clear"	, lambda: self.world.scenes.get("life").clear()),
			("Quit"		, lambda: self._quit())
		))

	def entry(self):
		self.world.window.set_caption("PyLife")
		pyglet.gl.glClearColor(0, 0, 0, 0)
		self.world.window.set_size(600, 600)
		self.world.window.center()


class Options(tkengine.TkOption):

	def __init__(self, world):
		world.set_options([
			["size", 25, 1, 100],
			["scale", 2, 1, 50],
			["speed", 3, 0, 5]
		])
		super(Options, self).__init__(world)
		self.key_handlers.update({
			pyglet.window.key.ESCAPE	: self.quit,
			pyglet.window.key.RETURN	: self.save,
		})
		pyglet.text.Label("Press return to save.",
			font_name="Times New Roman", font_size=30,
			x=140, y=60, batch=self.text_batch)
		pyglet.text.Label("PyLife",
			font_name="Times New Roman", font_size=56,
			x=10, y=500, batch=self.text_batch)


	def quit(self):
		self.world.transition("main")

	def save(self):
		self.world.set_options(self.updated_options)
		self.world.transition("main")

	def entry(self):
		self.world.window.set_caption("PyLife")



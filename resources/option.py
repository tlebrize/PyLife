from . import scene

class TkOption(scene.TkScene):

	def __init__(self, world):
		super(TkOption, self).__init__(world)
		self.updated_options = self.world.options
		if not len(self.updated_options):
			raise Exception("No world options given.")
		self.text_batch = pyglet.graphics.Batch()
		self.cursor = pyglet.text.Label(">", font_name="Times New Roman", font_size=36,
			x=100, y=300, batch=self.text_batch)
		self.cursor_pos = 0
		self._generate_text()
		self.key_handlers = {
			pyglet.window.key.ESCAPE	: self._quit(),
			pyglet.window.key.RETURN	: self._save(),
			pyglet.window.key.UP		: lambda: self._move_cursor(1),
			pyglet.window.key.DOWN		: lambda: self._move_cursor(-1),
			pyglet.window.key.LEFT		: lambda: self._update_value(1),
			pyglet.window.key.RIGHT		: lambda: self._update_value(-1)
		}

	def exit(self):
		self.updated_options = self.world.options
		self.cursor_pos = 0
		self.cursor.y = 300

	def on_draw(self):
		self.world.window.clear()
		self.text_batch.draw()

	def _update_value(self, value):
		selected = list(self.updated_options.keys())[self.cursor_pos]
		if isinstane(self.world.options[selected], bool):
			self.updated_options[selected] = not self.world.options[selected]
		else:
			self.updated_options[selected] += value

	def _move_cursor(self, direction):
		self.cursor_pos = (self.cursor_pos - direction) % len(self.updated_options)
		self.cursor.y = 300 - 40 * self.cursor_pos

	def _generate_text(self):
		options = self.updated_options.keys()
		for i, option in enumerate(options):
			pyglet.text.Label("{name}: {value}".format(**options),
				font_name="Times New Roman", font_size=36,
				x=140, y=300 - 40 * i, batch=self.text_batch)

	def _quit(self):
		self.world.transition("main")

	def _save(self):
		self.world.options.update(self.updated_options)
		print(self.world.options)
		self.world.transition("main")


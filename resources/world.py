import collections

class TkWorld(object):

	def __init__(self, window):
		self.window = window
		self.current = None
		self.scenes = {}
		self.options = []

	def get_options(self):
		options = []
		for key in self.options:
			options.append([key, getattr(self, key)])
		return options

	def set_options(self, new):
		for key, value in new:
			if key not in self.options:
				self.options.append(key)
			setattr(self, key, value)

	def transition(self, scene):
		if self.current:
			self.current.unload(self.window)
		self.current = self.scenes[scene]
		self.current.load(self.window)

	def add_scenes(self, new_scenes):
		self.scenes.update(new_scenes)

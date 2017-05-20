import pyglet

class TkScene(object):

	WINDOW_EVENTS = ["on_draw", "on_mouse_press", "on_mouse_release", "on_mouse_drag", "on_key_press"]

	def __init__(self, world):
		self.world = world

	def entry(self):
		pyglet.gl.glClearColor(0, 0, 0, 0)

	def load(self, window):
		for event in TkScene.WINDOW_EVENTS:
			if hasattr(self, event):
				window.__setattr__(event, self.__getattribute__(event))
		self.entry()

	def unload(self, window):
		for event in TkScene.WINDOW_EVENTS:
			if hasattr(self, event):
				window.__setattr__(event, lambda *args: False)
		if hasattr(self, "exit"):
			self.exit()
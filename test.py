import pyglet
from pyglet import gl

window = pyglet.window.Window()

cell_a = Cell(1, 1, (0.5, 0.5, 0.0))
cell_b = Cell(2, 2, (0.0, 0.5, 0.5))

@window.event
def on_draw():
	window.clear()
	cell_a.draw()
	cell_b.draw()

pyglet.app.run()


# x = 1
# y = 1
# # 5,5
# # 5, 55
# # 55, 55
# # 55, 5
# batch.add(4, pyglet.gl.GL_POLYGON, None,
# 	("v2i", (
# 		(5 * x) + 50 * x - 25, (5 * y) + 50 * y - 25,
# 		(5 * x) + 50 * x - 25, (5 * y) + 50 * y + 25,
# 		(5 * x) + 50 * x + 25, (5 * y) + 50 * y + 25,
# 		(5 * x) + 50 * x + 25, (5 * y) + 50 * y - 25
# 	)))
# x = 2
# y = 2
# # 65,5
# # 65, 55
# # 115, 55
# # 115, 5
# batch.add(4, pyglet.gl.GL_POLYGON, None,
# 	("v2i", (
# 		(5 * x) + 50 * x - 25, (5 * y) + 50 * y - 25,
# 		(5 * x) + 50 * x - 25, (5 * y) + 50 * y + 25,
# 		(5 * x) + 50 * x + 25, (5 * y) + 50 * y + 25,
# 		(5 * x) + 50 * x + 25, (5 * y) + 50 * y - 25
# 		)))

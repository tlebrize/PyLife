import pyglet, collections, tkengine
from resources.map import Map
from resources.menu import Menu, Options

def main():
	window = tkengine.TkWindow(caption="PyLife")
	world = tkengine.TkWorld(window, font='Times New Roman')
	main_menu = Menu(world)
	options = Options(world)
	life = Map(world)
	world.add_scenes({"main": main_menu, "life": life, "options": options})
	world.run("main")

if __name__ == "__main__":
	main()
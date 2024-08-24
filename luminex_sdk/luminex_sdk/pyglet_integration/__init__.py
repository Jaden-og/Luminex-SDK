import pyglet

def create_pyglet_window(width=800, height=600):
    window = pyglet.window.Window(width, height)
    return window

def draw_pyglet_rectangle(window, color, x, y, width, height):
    @window.event
    def on_draw():
        window.clear()
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_QUADS,
                                     [0, 1, 2, 3],
                                     ('v2f', (x, y, x + width, y, x + width, y + height, x, y + height)),
                                     ('c3B', color * 4))
    pyglet.app.run()

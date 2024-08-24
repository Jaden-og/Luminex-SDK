from .pygame_integration import init_pygame, draw_rectangle
from .pyglet_integration import create_pyglet_window, draw_pyglet_rectangle
from .opengl_integration import init_opengl, draw_opengl_square

__all__ = [
    "init_pygame",
    "draw_rectangle",
    "create_pyglet_window",
    "draw_pyglet_rectangle",
    "init_opengl",
    "draw_opengl_square"
]

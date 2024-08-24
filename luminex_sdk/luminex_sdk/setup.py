from setuptools import setup, find_packages

setup(
    name="luminex_sdk",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pygame",
        "pyglet",
        "PyOpenGL"
    ],
    description="Luminex SDK integrating Pygame, Pyglet, and PyOpenGL.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/luminex_sdk",
)

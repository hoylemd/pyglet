from game.asteroid import Asteroid

from game import resources


def test_init():
    sut = Asteroid(name="Asteroid", img=resources.asteroid_image)

    assert sut is not None

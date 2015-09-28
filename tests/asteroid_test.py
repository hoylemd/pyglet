from game.asteroid import Asteroid

from game import resources


def test_init():
    sut = Asteroid(name="Asteroid", img=resources.asteroid_image)

    assert sut is not None


def test_handle_collision__full_size():
    raise NotImplementedError


def test_handle_collision__quarter_size():
    raise NotImplementedError

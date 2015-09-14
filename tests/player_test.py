from pyglet.window import key
from game.player import Player
from game import resources


def test_key_press__left():
    sut = Player(img=resources.player_image, x=200, y=300)

    sut.on_key_press(key.LEFT, None)

    assert sut.keys['left']

    sut.on_key_release(key.LEFT, None)

    assert not sut.keys['left']


def test_key_press__right():
    sut = Player(img=resources.player_image, x=200, y=300)

    sut.on_key_press(key.RIGHT, None)

    assert sut.keys['right']

    sut.on_key_release(key.RIGHT, None)

    assert not sut.keys['right']


def test_key_press__up():
    sut = Player(img=resources.player_image, x=200, y=300)

    sut.on_key_press(key.UP, None)

    assert sut.keys['up']

    sut.on_key_release(key.UP, None)

    assert not sut.keys['up']


def test_key_press__down():
    sut = Player(img=resources.player_image, x=200, y=300)

    sut.on_key_press(key.DOWN, None)

    assert sut.keys['down']

    sut.on_key_release(key.DOWN, None)

    assert not sut.keys['down']


def test_key_press__space():
    sut = Player(img=resources.player_image, x=200, y=300)

    sut.on_key_press(key.SPACE, None)

    assert sut.signals['recenter']

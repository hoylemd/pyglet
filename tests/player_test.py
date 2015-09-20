from pyglet.window import key
from game.player import Player
from game import resources
from tests.scaffolding import fps_to_s, eq_within_epsilon


def test_init__initial_values():
    sut = Player(img=resources.player_image)

    assert sut.thrust == 200.0
    assert sut.maneuvering_thrust == 360.0

    assert sut.x == 0.0
    assert sut.y == 0.0

    assert sut.center_x == 0.0
    assert sut.center_y == 0.0

    for sut_key in sut.keys:
        assert not sut.keys[sut_key]

    for signal in sut.signals:
        assert not sut.signals[signal]


def test_init__specified_values():
    sut = Player(img=resources.player_image, x=123.4, y=421.54, thrust=150.0,
                 maneuvering_thrust=500.0)

    assert sut.thrust == 150.0
    assert sut.maneuvering_thrust == 500.0

    assert sut.x == 123.4
    assert sut.y == 421.54

    assert sut.center_x == 123.4
    assert sut.center_y == 421.54


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


def set_up_sluggish_player():
    return Player(img=resources.player_image, x=200.0, y=300.0, thrust=10.0,
                  maneuvering_thrust=15.0)


def test_init__sluggish():
    sut = set_up_sluggish_player()

    assert sut.rotation_speed == 0.0
    assert sut.rotation == 0.0
    assert sut.velocity_x == 0.0
    assert sut.velocity_y == 0.0
    assert sut.x == 200.0
    assert sut.y == 300.0


def test_update__turn_right():
    sut = set_up_sluggish_player()

    # turn right
    sut.on_key_press(key.RIGHT, None)

    sut.update(fps_to_s(60))  # one 60 fps frame

    assert sut.rotation_speed == 0.25
    assert eq_within_epsilon(sut.rotation, 0.0021, 0.0001)

    sut.update(fps_to_s(60) * 59)  # finish this second

    sut.on_key_release(key.RIGHT, None)

    assert sut.rotation_speed == 15.0
    assert eq_within_epsilon(sut.rotation, 7.5)

    sut.update(1.0)  # one second

    assert sut.rotation_speed == 15.0
    assert eq_within_epsilon(sut.rotation, 22.5)


def test_update__turn_left():
    sut = set_up_sluggish_player()

    # turn left
    sut.on_key_press(key.LEFT, None)

    sut.update(fps_to_s(60) * 1.5)

    assert sut.rotation_speed == -0.375
    assert eq_within_epsilon(sut.rotation, 359.9953, 0.0001)

    sut.update(fps_to_s(60) * 58.5)  # finish this second

    sut.on_key_release(key.LEFT, None)

    assert sut.rotation_speed == -15
    assert eq_within_epsilon(sut.rotation, 352.5)

    sut.update(1.0)  # one second

    assert sut.rotation_speed == -15
    assert eq_within_epsilon(sut.rotation, 337.5)


def test_update__SAS():
    sut = set_up_sluggish_player()

    # start turning
    sut.on_key_press(key.RIGHT, None)

    sut.update(1.0)  # one 60 fps frame

    sut.on_key_release(key.RIGHT, None)

    assert sut.rotation_speed == 15.0
    assert eq_within_epsilon(sut.rotation, 7.5)

    # engage SAS
    sut.on_key_press(key.DOWN, None)

    sut.update(0.5)  # stabilize for half a second

    assert sut.rotation_speed == 7.5
    assert eq_within_epsilon(sut.rotation, 13.12)

    sut.on_key_release(key.DOWN, None)

    sut.update(0.5)  # drift for half a second

    assert sut.rotation_speed == 7.5
    assert eq_within_epsilon(sut.rotation, 16.87)

    sut.on_key_press(key.DOWN, None)

    sut.update(1.0)  # stabilize for a full second

    assert sut.rotation_speed == 0.0
    assert eq_within_epsilon(sut.rotation, 20.62)


def test_update__thrust():
    sut = set_up_sluggish_player()

    # artificially set rotation
    sut.rotation = 45.0

    assert sut.velocity_x == 0.0
    assert sut.velocity_y == 0.0
    assert sut.x == 200.0
    assert sut.y == 300.0

    # engage thrust
    sut.on_key_press(key.UP, None)
    sut.update(1.0)

    assert eq_within_epsilon(sut.velocity_x, 7.08)
    assert eq_within_epsilon(sut.velocity_y, 7.08)
    assert eq_within_epsilon(sut.x, 203.54)
    assert eq_within_epsilon(sut.y, 303.54)

    # stop thrust and drift
    sut.on_key_release(key.UP, None)
    sut.update(2.0)

    assert eq_within_epsilon(sut.velocity_x, 7.08)
    assert eq_within_epsilon(sut.velocity_y, 7.08)
    assert eq_within_epsilon(sut.x, 217.68)
    assert eq_within_epsilon(sut.y, 317.68)

    # stop altogether
    sut.rotation += 180.0
    sut.on_key_press(key.UP, None)
    sut.update(1.0)

    assert eq_within_epsilon(sut.velocity_x, 0.0)
    assert eq_within_epsilon(sut.velocity_y, 0.0)
    assert eq_within_epsilon(sut.x, 221.22)
    assert eq_within_epsilon(sut.y, 321.22)

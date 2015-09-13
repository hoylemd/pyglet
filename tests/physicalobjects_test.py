from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from game.physicalobjects import InertialObject
from tests.scaffolding import fixtures


def test_init__motionless():
    sut = InertialObject(img=fixtures['player_image'])

    assert sut.velocity_x == 0.0
    assert sut.velocity_y == 0.0
    assert sut.rotation_speed == 0.0


def test_loop_position__origin():
    sut = InertialObject(img=fixtures['player_image'])

    assert sut.x == 0
    assert sut.y == 0

    sut.loop_position()

    assert sut.x == 0
    assert sut.y == 0


def test_loop_position__on_screen():
    sut = InertialObject(img=fixtures['player_image'])

    sut.x = 56.3
    sut.y = 174.23

    sut.loop_position()

    assert sut.x == 56.3
    assert sut.y == 174.23


def test_loop_position__off_top():
    sut = InertialObject(img=fixtures['player_image'])

    sut.x = 56.3
    sut.y = WINDOW_HEIGHT + 30.0

    sut.loop_position()

    assert sut.x == 56.3
    assert sut.y == -25.0


def test_loop_position__off_bottom():
    sut = InertialObject(img=fixtures['player_image'])

    sut.x = 56.3
    sut.y = -30.0

    sut.loop_position()

    assert sut.x == 56.3
    assert sut.y == WINDOW_HEIGHT + 25.0


def test_loop_position__off_left():
    sut = InertialObject(img=fixtures['player_image'])

    sut.x = -30.0
    sut.y = 156.8

    sut.loop_position()

    assert sut.x == WINDOW_WIDTH + 25.0
    assert sut.y == 156.8


def test_loop_position__off_right():
    sut = InertialObject(img=fixtures['player_image'])

    sut.x = WINDOW_WIDTH + 30.0
    sut.y = 156.8

    sut.loop_position()

    assert sut.x == -25.0
    assert sut.y == 156.8

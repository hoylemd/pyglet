import pysteroids.game.utils as utils


def test_distance__x_only():
    assert utils.distance((0.0, 0.0), (1.0, 0.0)) == 1


def test_distance__y_only():
    assert utils.distance((0.0, 0.0), (0.0, 7.3)) == 7.3


def test_distance__diagonal():
    print utils.distance((100.0, -3.2), (-0.750, 34.0))
    rounded = "{:.4f}".format(utils.distance((100.0, -3.2), (-0.750, 34.0)))
    assert rounded == '107.3983'

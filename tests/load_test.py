from game import load
from game import utils


def test_asteroids__3():
    results = load.asteroids(3, (100, 100))

    assert len(results) == 3


def test_asteroids__20_no_collosions():
    results = load.asteroids(3, (100, 100))

    for result in results:
        assert utils.distance(result.position, (100, 100)) >= 100

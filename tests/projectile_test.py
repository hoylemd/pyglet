from game.projectile import Projectile
from game import resources


def test_init():
    sut = Projectile(name="bullet", img=resources.bullet_image, x=100, y=200)

    assert sut is not None

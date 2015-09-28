from random import randint
from physicalobjects import InertialObject
from util import normalize_degrees


class Asteroid(InertialObject):
    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(
            vulnerable=True, damaging=True, explosive_force=70.0,
            *args, **kwargs)


    def handle_collision(self, other):
        super(Asteroid, self).handle_collision(other)

        if self.dead and self.scale > 0.25:
            num_fragments = randint(2, 3)

            for i in xrange(num_fragments):
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = normalize_degrees(
                    self.rotation + randint(-360.0, 360.0))

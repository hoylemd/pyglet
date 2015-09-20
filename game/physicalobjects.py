import pyglet
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
import game.utils as utils


class InertialObject(pyglet.sprite.Sprite):

    def __init__(self, name="", *args, **kwargs):
        super(InertialObject, self).__init__(*args, **kwargs)

        self.name = name
        self.dead = False
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.rotation_speed = 0.0

    def loop_position(self):
        x_min_margin = - self.image.width / 2.0
        y_min_margin = - self.image.height / 2.0
        x_max_margin = WINDOW_WIDTH - x_min_margin
        y_max_margin = WINDOW_HEIGHT - y_min_margin

        if self.x < x_min_margin:
            self.x = x_max_margin
        elif self.x > x_max_margin:
            self.x = x_min_margin

        if self.y < y_min_margin:
            self.y = y_max_margin
        elif self.y > y_max_margin:
            self.y = y_min_margin

    def collides_with(self, other):
        return False

    def handle_collision(self, other):
        print "collosion between %s and %s" % self.name, other.name

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += self.rotation_speed * dt
        self.rotation = utils.normalize_degrees(self.rotation)

        self.loop_position()

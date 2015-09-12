import pyglet
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.rotation_speed = 0.0

    def loop_position(self):
        x_min_margin = - self.image.width / 2
        y_min_margin = - self.image.height / 2
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

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.rotation += (self.rotation_speed * dt) % 360

        self.loop_position()

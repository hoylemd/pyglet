import math
from pyglet.window import key
from physicalobjects import InertialObject


class Player(InertialObject):
    def __init__(self, x=0.0, y=0.0, thrust=300.0,
                 maneuvering_thrust=360.0, *args, **kwargs):

        super(Player, self).__init__(x=x, y=y, *args, **kwargs)

        self.thrust = thrust
        self.maneuvering_thrust = maneuvering_thrust

        self.center_x = x
        self.center_y = y

        self.keys = {'left': False, 'up': False, 'right': False, 'down': False}
        self.signals = {'recenter': False}

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = True
        if symbol == key.UP:
            self.keys['up'] = True
        if symbol == key.RIGHT:
            self.keys['right'] = True
        if symbol == key.DOWN:
            self.keys['down'] = True

        if symbol == key.SPACE:
            self.signals['recenter'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.keys['left'] = False
        if symbol == key.UP:
            self.keys['up'] = False
        if symbol == key.RIGHT:
            self.keys['right'] = False
        if symbol == key.DOWN:
            self.keys['down'] = False

    def update(self, dt):
        rotational_dv = self.maneuvering_thrust * dt
        propulsive_dv = self.thrust * dt

        if self.keys['right']:
            self.rotation_speed += rotational_dv
        if self.keys['left']:
            self.rotation_speed -= rotational_dv
        if self.keys['up']:
            angle_radians = math.radians(self.rotation)
            force_x = math.sin(angle_radians) * propulsive_dv
            force_y = math.cos(angle_radians) * propulsive_dv
            self.velocity_x += force_x
            self.velocity_y += force_y
        if self.keys['down']:
            direction = 1.0
            if self.rotation_speed < 0:
                direction = -1.0
            abs_rotation = self.rotation_speed * direction
            self.rotation_speed = direction * (abs_rotation - rotational_dv)
            if (direction * self.rotation_speed) < 0:
                self.rotation_speed = 0

        if self.signals['recenter']:
            self.x = self.center_x
            self.y = self.center_y
            self.velocity_x = 0.0
            self.velocity_y = 0.0
            self.rotation = 0.0
            self.rotation_speed = 0.0
            self.signals['recenter'] = False

        super(Player, self).update(dt)

import math
from pyglet.window import key
from physicalobjects import InertialObject


class Player(InertialObject):
    def __init__(self, x=0.0, y=0.0, thrust=200.0,
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

        modified_rot_speed = self.rotation_speed
        if self.keys['right']:
            modified_rot_speed += rotational_dv
        if self.keys['left']:
            modified_rot_speed -= rotational_dv
        if self.keys['down']:
            direction = 1.0
            if self.rotation_speed < 0:
                direction = -1.0
            abs_rotation = modified_rot_speed * direction
            modified_rot_speed = direction * (abs_rotation - rotational_dv)
            if (direction * modified_rot_speed) < 0:
                modified_rot_speed = 0.0

        # interpolate accelerated rotation change
        self.rotation_speed = (modified_rot_speed + self.rotation_speed) / 2.0

        modified_vx = self.velocity_x
        modified_vy = self.velocity_y
        if self.keys['up']:
            angle_radians = math.radians(self.rotation)
            modified_vx += math.sin(angle_radians) * propulsive_dv
            modified_vy += math.cos(angle_radians) * propulsive_dv

        # iterpolate accelerated velocity change
        self.velocity_x = (modified_vx + self.velocity_x) / 2.0
        self.velocity_y = (modified_vy + self.velocity_y) / 2.0

        if self.signals['recenter']:
            self.x = self.center_x
            self.y = self.center_y
            self.velocity_x = 0.0
            self.velocity_y = 0.0
            self.rotation = 0.0
            self.rotation_speed = 0.0
            self.signals['recenter'] = False

        super(Player, self).update(dt)

        self.rotation_speed = modified_rot_speed
        self.velocity_x = modified_vx
        self.velocity_y = modified_vy

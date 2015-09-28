from physicalobjetcts import InertialObject


class Projectile(InertialObject):
    def __init__(self, *args, **kwargs):
        super(Projectile, self).__init__(*args, **kwargs)

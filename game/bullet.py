from physicalobjetcts import InertialObject


class Bullet(InertialObject):
    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(*args, **kwargs)

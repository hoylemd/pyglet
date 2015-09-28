from physicalobjects import InertialObject


class Asteroid(InertialObject):
    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(*args, **kwargs)

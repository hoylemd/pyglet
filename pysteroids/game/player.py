from physicalobject import PhysicalObject
import resources


class Player(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(
            img=resources.player_image, *args, **kwargs)

        self.thrust = 300.0
        self.maneuvering_thrust = 200.0

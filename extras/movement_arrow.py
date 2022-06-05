import math

from core_ext.object3d import Object3D


class MovementArrow(Object3D):
    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    def __init__(self, units_per_second=1, degrees_per_second=60):
        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)
    def remove(self, child):
        self._look_attachment.remove(child)

    def update(self, input_object, delta_time):
        # move_amount = self._units_per_second * delta_time
        # rotate_amount = self._degrees_per_second * (math.pi / 180) * delta_time
        # move_amount = self._units_per_second * delta_time
        # rotate_amount = self._degrees_per_second * (math.pi / 180) * delta_time
        self.set_position([(input_object._mouse_pos[0]/400-1)*5, -(input_object._mouse_pos[1]/300-1)*5, 3])


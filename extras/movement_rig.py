import math

from core_ext.object3d import Object3D


class MovementRig(Object3D):
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
        self.initial = self._look_attachment.local_matrix

        # Customizable key mappings.
        # Defaults: W, A, S, D, R, F (move), Q, E (turn), T, G (look)
        self.KEY_MOVE_FORWARDS = "w"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_MOVE_DOWN = "f"
        self.KEY_TURN_LEFT = "q"
        self.KEY_TURN_RIGHT = "e"
        self.KEY_LOOK_UP = "t"
        self.KEY_LOOK_DOWN = "g"
        self.SHOOT = "mouse1"
        self.RELOAD = "r"
        self.shooting = False
        self.power = 0
        self.ready = True

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)
    def remove(self, child):
        self._look_attachment.remove(child)

    def isShooting(self):
        return self.shooting
        
    def setShooting(self, shoot):
        self.shooting = shoot

    def isReady(self):
        return self.ready

    def getPower(self):
        return self.power
    
    def setPower(self, power):
        self.power = power

    def getInitalMatrix(self):
        return self.initial

    def update(self, input_object, delta_time):
        move_amount = self._units_per_second * delta_time
        if input_object.is_key_pressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -move_amount)
        if input_object.is_key_pressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, move_amount)
        if input_object.is_key_pressed(self.KEY_MOVE_LEFT):
            self.translate(-move_amount, 0, 0)
        if input_object.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.translate(move_amount, 0, 0)
        if input_object.is_key_pressed(self.SHOOT):
            self.power += 0.5
            if self.power > 100:
                self.power=100
        if input_object.is_key_up(self.SHOOT):
            self.shooting = True
            self.ready = False

        if input_object.is_key_pressed(self.RELOAD):
            self.shooting = False
            self.ready = True
            self.power = 0
        if input_object.is_key_pressed(self.KEY_MOVE_DOWN):
            self._look_attachment.set_local_matrix(self.initial)
        self._look_attachment.rotate_x(-1 * (math.pi / 180) * (input_object.mouse_position[1]/300-1))
        self._look_attachment.rotate_y(-1 * (math.pi / 180) * (input_object.mouse_position[0]/400-1))
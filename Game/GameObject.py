import pyxel

from Engine.Enums import CollisionType
from Engine.Managers import UpdateManager, DrawManager
class GameObject:
    def __init__(self, object_id, x, y, width, height, color = 7):
        self.object_id = object_id
        self.active = True
        self.type = None
        self.collision_type = CollisionType.NONE
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 1
        self.color = color
        UpdateManager.add_updatable(self)
        DrawManager.add_drawable(self)

    def is_active(self):
        return self.active

    def handle_movement(self):
        pass

    def handle_screen_collisions(self):
        pass

    def add_collision_type(self, collision_type):
        self.collision_type = self.collision_type | collision_type

    def can_collide_with(self, other):
        return (self.collision_type & other.type) != 0

    def does_collide(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y

        delta_x = abs(distance_x) - (self.width * 0.5 + other.width * 0.5)
        if delta_x > 0:
            return False

        delta_y = abs(distance_y) - (self.height * 0.5 + other.height * 0.5)
        if delta_y > 0:
            return False

        return True

    def on_collision(self, other):
        pass

    def update(self):
        self.handle_movement()
        self.handle_screen_collisions()

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, self.color)
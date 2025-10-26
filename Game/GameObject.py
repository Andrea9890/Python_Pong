import pyxel

from Engine.Managers import UpdateManager, DrawManager


class GameObject:
    def __init__(self, object_id, x, y, width, height):
        self.object_id = object_id
        self.active = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 1
        UpdateManager.add_updatable(self)
        DrawManager.add_drawable(self)

    def handle_movement(self):
        pass

    def handle_screen_collisions(self):
        pass

    def is_active(self):
        return self.active

    def update(self):
        self.handle_movement()
        self.handle_screen_collisions()

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 7)
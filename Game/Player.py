import pyxel

from Engine.Enums import Direction
from Engine.Managers import ScoreManager
from Game.GameObject import GameObject

class Player(GameObject):
    def __init__(self, object_id, x, y, width, height, direction):
        super().__init__(object_id, x, y, width, height)
        self.direction = direction
        self.speed_y = 2
        ScoreManager.register_player(object_id)

    # Player movement
    def handle_movement(self):
        match self.direction:
            case Direction.LEFT:
                if pyxel.btn(pyxel.KEY_W):
                    self.y -= self.speed_y
                if pyxel.btn(pyxel.KEY_S):
                    self.y += self.speed_y
            case Direction.RIGHT:
                if pyxel.btn(pyxel.KEY_UP):
                    self.y -= self.speed_y
                if pyxel.btn(pyxel.KEY_DOWN):
                    self.y += self.speed_y

    def handle_screen_collision(self):
        if self.y - self.height * 0.5 < 0:
            self.y = self.height * 0.5
        elif self.y + self.height * 0.5 > pyxel.height:
            self.y = pyxel.height - self.height * 0.5

    ### Pyxel callbacks ###
    def update(self):
        self.handle_movement()
        self.handle_screen_collision()

    def draw(self):
        pyxel.rect(self.x - self.width * 0.5, self.y - self.height * 0.5, self.width, self.height, 7)
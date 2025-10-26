import pyxel

from Engine.Enums import Direction, CollisionType
from Engine.Managers import ScoreManager, CollisionManager
from Game.GameObject import GameObject

class Player(GameObject):
    def __init__(self, object_id, x, y, width, height, direction, color = 7):
        super().__init__(object_id, x, y, width, height, color)
        self.direction = direction
        self.speed_y = 2
        self.collision_enabled = True
        self.type = CollisionType.PLAYER
        self.add_collision_type(CollisionType.BALL)
        CollisionManager.add_collidable(self)
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
        pyxel.rect(self.x - self.width * 0.5, self.y - self.height * 0.5, self.width, self.height, self.color)
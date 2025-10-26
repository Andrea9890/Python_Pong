import pyxel
import numpy as np

from Engine.Enums import Direction, CollisionType
from Engine.Managers import EventManager, ScoreManager, CollisionManager
from Game.GameObject import GameObject

class Ball(GameObject):
    def __init__(self, object_id, x, y, width, height, speed_x, speed_y,color):
        super().__init__(object_id, x, y, width, height,color)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.collision_enabled = True
        self.type = CollisionType.BALL
        self.add_collision_type(CollisionType.PLAYER)
        CollisionManager.add_collidable(self)

        EventManager.subscribe("match_start", self.on_match_start)

    def handle_movement(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def handle_screen_collisions(self):
        if self.x < self.width * 0.5:
            ScoreManager.update_score("Player2")
            EventManager.publish("score_changed", side = Direction.LEFT)
            self.speed_x = 0
            self.speed_y = 0
            self.x = 100
            self.y = 60

        if self.x > (pyxel.width - 1) - self.width * 0.5:
            ScoreManager.update_score("Player1")
            EventManager.publish("score_changed", side=Direction.RIGHT)
            self.speed_x = 0
            self.speed_y = 0
            self.x = 60
            self.y = 60

        if self.y < self.height * 0.5 or self.y > (pyxel.height - 1) - self.height * 0.5:
            self.speed_y *= -1

    def on_match_start(self, side):
        match side:
            case Direction.LEFT:
                self.speed_x = -1
                self.speed_y = np.random.choice([-1, 1])

            case Direction.RIGHT:
                self.speed_x = 1
                self.speed_y = np.random.choice([-1, 1])

    def on_collision(self, other):
        self.speed_x *= -1

    def update(self):
        self.handle_movement()
        self.handle_screen_collisions()

    def draw(self):
        pyxel.rect(self.x - self.width * 0.5, self.y - self.height * 0.5, self.width, self.height, self.color)
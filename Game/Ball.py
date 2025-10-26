import pyxel
import numpy as np

from Engine.Enums import Direction
from Engine.Managers import EventManager, ScoreManager
from Game.GameObject import GameObject

class Ball(GameObject):
    def __init__(self, object_id, x, y, width, height, speed_x, speed_y,):
        super().__init__(object_id, x, y, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def handle_movement(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def handle_screen_collisions(self):
        if self.x < 0:
            ScoreManager.update_score("Player2")
            EventManager.publish("score_changed", side = Direction.LEFT)
            self.speed_x = 0
            self.speed_y = 0
            self.x = 100
            self.y = 60
            EventManager.subscribe("match_start", self.on_match_start)

        if self.x > pyxel.width - 1:
            ScoreManager.update_score("Player1")
            EventManager.publish("score_changed", side=Direction.RIGHT)
            self.speed_x = 0
            self.speed_y = 0
            self.x = 60
            self.y = 60
            EventManager.subscribe("match_start", self.on_match_start)

        if self.y < 0 or self.y > pyxel.height - 1:
            self.speed_y *= -1

    def on_match_start(self, side):
        match side:
            case Direction.LEFT:
                self.speed_x = -1
                self.speed_y = np.random.choice([-1, 1])

            case Direction.RIGHT:
                self.speed_x = 1
                self.speed_y = np.random.choice([-1, 1])

    def update(self):
        self.handle_movement()
        self.handle_screen_collisions()

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 7)
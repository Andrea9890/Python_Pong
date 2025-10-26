import math

import pyxel

from Engine.Managers import ScoreManager, DrawManager, UpdateManager, EventManager
from Game.GameObject import GameObject

class CountdownUI(GameObject):
    def __init__(self, object_id, x, y, width, height):
        super().__init__(object_id, x, y, width, height)
        self.countdown_timer = 3
        self.side = None
        EventManager.subscribe("score_changed", self.on_score_changed)
        UpdateManager.remove_updatable(self)
        DrawManager.remove_drawable(self)

    def on_score_changed(self, side):
        self.side = side
        self.reset()
        self.show()

    def hide(self):
        self.active = False
        UpdateManager.remove_updatable(self)
        DrawManager.remove_drawable(self)

    def show(self):
        self.active = True
        UpdateManager.add_updatable(self)
        DrawManager.add_drawable(self)

    def reset(self):
        self.countdown_timer = 3

    def update(self):
        self.countdown_timer -= 0.016
        if self.countdown_timer <= 0:
            self.hide()
            EventManager.publish("match_start", side=self.side)

    def draw(self):
        pyxel.text(self.x, self.y, f"{math.ceil(self.countdown_timer)}", 7)
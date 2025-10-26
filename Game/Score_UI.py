import pyxel

from Engine.Enums import Direction
from Engine.Managers import ScoreManager, EventManager
from Game.GameObject import GameObject

class ScoreUI(GameObject):
    def __init__(self, object_id, x, y, width, height):
        super().__init__(object_id, x, y, width, height)
        self.score1 = ScoreManager.get_score("Player1")
        self.score2 = ScoreManager.get_score("Player2")
        EventManager.subscribe("score_changed", self.on_score_changed)

    def on_score_changed(self, side):
        match side:
            case Direction.LEFT:
                self.score2 = ScoreManager.get_score("Player2")
            case Direction.RIGHT:
                self.score1 = ScoreManager.get_score("Player1")

    def update(self):
        pass

    def draw(self):
        pyxel.text(self.x, self.y, f"{self.score1} - {self.score2}", 7)
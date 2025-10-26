import pyxel
from Game import Ball as b, Player as p
from Engine.Managers import DrawManager, UpdateManager, ScoreManager
from Engine.Enums import Direction
from Game.Countdown_UI import CountdownUI
from Game.Score_UI import ScoreUI

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, "PONG")

        self.player1 = p.Player("Player1", 10, SCREEN_HEIGHT * 0.5, 3, 15, Direction.LEFT)
        self.player2 = p.Player("Player2", 150, SCREEN_HEIGHT * 0.5, 3, 15, Direction.RIGHT)
        self.ball = b.Ball("Ball", SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, 1, 1, 1, 1)
        self.score_ui = ScoreUI("ScoreUI", 5, 5, 100, 100)
        self.countdown_ui = CountdownUI("CountdownUI", 100, 100, 100, 100)

        pyxel.run(self.update, self.draw)

    def update(self):
        UpdateManager.update()
        #CollisionManager.handle_collisions()

    def draw(self):
        pyxel.cls(0)
        DrawManager.draw()

App()
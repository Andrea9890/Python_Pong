import pyxel
from Game import Ball as b, Player as p
from Engine.Managers import DrawManager, UpdateManager, ScoreManager, CollisionManager
from Engine.Enums import Direction
from Game.Countdown_UI import CountdownUI
from Game.Score_UI import ScoreUI

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
PLAYER_WIDTH = 4
PLAYER_HEIGHT = 15
BALL_SIZE = 2
BALL_SPEED_X = 1
BALL_SPEED_Y = 1

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, "PONG")

        self.player1 = p.Player("Player1", 10, SCREEN_HEIGHT * 0.5, PLAYER_WIDTH, PLAYER_HEIGHT, Direction.LEFT, 5)
        self.player2 = p.Player("Player2", 150, SCREEN_HEIGHT * 0.5, PLAYER_WIDTH, PLAYER_HEIGHT, Direction.RIGHT, 8)
        self.ball = b.Ball("Ball", SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, BALL_SIZE, BALL_SIZE, BALL_SPEED_Y, BALL_SPEED_Y, 7)
        self.score_ui = ScoreUI("ScoreUI", 5, 5, 0, 0)
        self.countdown_ui = CountdownUI("CountdownUI", SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, 0, 0)

        pyxel.run(self.update, self.draw)

    def update(self):
        UpdateManager.update()
        CollisionManager.check_collisions()

    def draw(self):
        pyxel.cls(0)
        DrawManager.draw()

App()
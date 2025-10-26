from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class CollisionType(Enum):
    NONE = 1
    PLAYER = 2
    BALL = 3
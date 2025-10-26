from enum import Enum, IntFlag

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class CollisionType(IntFlag):
    NONE = 0
    PLAYER = 1
    BALL = 2
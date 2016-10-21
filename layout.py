import random
from collections import namedtuple

Marker = namedtuple('Marker', 'water, hit, ship, miss')
Board = namedtuple('Board', 'side, top, corner')

marker = Marker(' ', '*', 'x', 'o')
board = Board('|', '-', '+')

competition = False

rows = 12
columns = 14

ships = [
    [ [2,1], [2,8] ], # size 5 aircraft_carrier
    [ [5,4], [9,4] ], # size 4 battleship
    [ [0,1], [0,5] ], # size 3 submarine
    [ [3,8], [6,8] ], # size 3 cruiser
    [ [4,2], [8,2] ], # size 2 destroyer
]

current = lambda: [ random.randint(-1, 1) for _ in range(2) ]


# grid.py
import json
from typing import Dict, Tuple
from room_generation import generate_room

class Tile:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.discovered = False
        self.data = None

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles: Dict[Tuple[int, int], Tile] = {}
        self.player_x = width // 2  # Start in the middle
        self.player_y = height // 2

    def get_tile(self, x: int, y: int) -> Tile:
        if (x, y) not in self.tiles:
            self.tiles[(x, y)] = Tile(x, y)
        return self.tiles[(x, y)]

    def generate_tile_data(self, x: int, y: int, model):
        tile = self.get_tile(x, y)
        if not tile.discovered:
            tile.data = generate_room(x, y, model)
            tile.discovered = True
        return tile.data

    def move_player(self, direction: str) -> Tuple[int, int]:
        new_x, new_y = self.player_x, self.player_y
        if direction == "north" and self.player_y > 0:
            new_y -= 1
        elif direction == "south" and self.player_y < self.height - 1:
            new_y += 1
        elif direction == "west" and self.player_x > 0:
            new_x -= 1
        elif direction == "east" and self.player_x < self.width - 1:
            new_x += 1
        
        if (new_x, new_y) != (self.player_x, self.player_y):
            self.player_x, self.player_y = new_x, new_y
            return True
        return False
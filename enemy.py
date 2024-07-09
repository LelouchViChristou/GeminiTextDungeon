import json
import random
from api_setup import modelRoomGen

class Enemy:
    def __init__(self, name: str, type: str, level: int, hp: int, 
                 description: str, abilities: list,
                 strength: int = None, dexterity: int = None, constitution: int = None,
                 wisdom: int = None, intelligence: int = None, charisma: int = None,
                 loot: list = None):
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp
        self.description = description
        self.abilities = abilities
        self.strength = strength if strength is not None else self.roll_attribute()
        self.dexterity = dexterity if dexterity is not None else self.roll_attribute()
        self.constitution = constitution if constitution is not None else self.roll_attribute()
        self.wisdom = wisdom if wisdom is not None else self.roll_attribute()
        self.intelligence = intelligence if intelligence is not None else self.roll_attribute()
        self.charisma = charisma if charisma is not None else self.roll_attribute()
        self.loot = loot if loot is not None else []

    def roll_dice(self, num_dice: int, sides: int) -> int:
        """Rolls the specified number of dice with the given sides and returns the sum."""
        return sum(random.randint(1, sides) for _ in range(num_dice))

    def roll_attribute(self) -> int:
        """Rolls 3d6 to generate an attribute score."""
        return self.roll_dice(3, 6)

    def get_status(self):
        """Returns a summary of the enemy's current status."""
        return {
            "name": self.name,
            "type": self.type,
            "level": self.level,
            "hp": self.hp,
            "description": self.description,
            "abilities": self.abilities,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "wisdom": self.wisdom,
            "intelligence": self.intelligence,
            "charisma": self.charisma,
            "loot": self.loot
        }

def generate_enemy(enemy_type: str = None, level: int = None) -> Enemy:
    prompt = f"""
    Create a detailed enemy description for a fantasy RPG game.
    
    Enemy Type: {enemy_type if enemy_type else "Any"}
    Level: {level if level else "Any"}

    Using this JSON schema:
      Enemy = {{
        "name": str,
        "type": str,
        "level": int,
        "hp": int,
        "description": str,
        "abilities": list[str],
        "strength": int,
        "dexterity": int,
        "constitution": int,
        "wisdom": int,
        "intelligence": int,
        "charisma": int,
        "loot": list[str]
      }}
    Return an `Enemy`
    """
    response = modelRoomGen.generate_content(prompt)
    enemy_data = json.loads(response.text)

    return Enemy(
        name=enemy_data["name"],
        type=enemy_data["type"],
        level=enemy_data["level"],
        hp=enemy_data["hp"],
        description=enemy_data["description"],
        abilities=enemy_data["abilities"],
        strength=enemy_data["strength"],
        dexterity=enemy_data["dexterity"],
        constitution=enemy_data["constitution"],
        wisdom=enemy_data["wisdom"],
        intelligence=enemy_data["intelligence"],
        charisma=enemy_data["charisma"],
        loot=enemy_data["loot"]
    )
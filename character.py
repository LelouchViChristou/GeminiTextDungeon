import json
import random
from api_setup import modelRoomGen

class Character:
    def __init__(self, name: str, age: str, gender: str, level: int, hp: int, alignment: str,
                 description: str, background: str, wealth: int = None,
                 strength: int = None, dexterity: int = None, constitution: int = None,
                 wisdom: int = None, intelligence: int = None, charisma: int = None,
                 classs: str = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.hp = hp
        self.alignment = alignment
        self.description = description
        self.background = background
        self.wealth = wealth if wealth is not None else self.roll_wealth()
        self.strength = strength if strength is not None else self.roll_attribute()
        self.dexterity = dexterity if dexterity is not None else self.roll_attribute()
        self.constitution = constitution if constitution is not None else self.roll_attribute()
        self.wisdom = wisdom if wisdom is not None else self.roll_attribute()
        self.intelligence = intelligence if intelligence is not None else self.roll_attribute()
        self.charisma = charisma if charisma is not None else self.roll_attribute()
        self.classs = classs

    def roll_dice(self, num_dice: int, sides: int) -> int:
        """Rolls the specified number of dice with the given sides and returns the sum."""
        return sum(random.randint(1, sides) for _ in range(num_dice))

    def roll_wealth(self) -> int:
        """Rolls 4d10 for starting gold pieces (wealth)."""
        return self.roll_dice(4, 10)

    def roll_attribute(self) -> int:
        """Rolls 4d6 and drops the lowest die to generate an attribute score."""
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])  # Drop the lowest roll

    def get_status(self):
        """Returns a summary of the character's current status."""
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "level": self.level,
            "hp": self.hp,
            "alignment": self.alignment,
            "description": self.description,
            "background": self.background,
            "wealth": self.wealth,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "wisdom": self.wisdom,
            "intelligence": self.intelligence,
            "charisma": self.charisma,
            "class": self.classs
        }

def generate_character() -> Character:
    userInput=input("> ")
    prompt = f"""
    Create a detailed character description for a fantasy RPG game based on the name and the following description:
    {userInput}
   

    Using this JSON schema:
      Character = {{
        "name": str,
        "age": str,
        "gender": str,
        "level": int,
        "hp": int,
        "alignment": str,
        "description": str,
        "background": str,
        "wealth": int,
        "strength": int,
        "dexterity": int,
        "constitution": int,
        "wisdom": int,
        "intelligence": int,
        "charisma": int,
        "class": str
      }}
    Return a `Character`
    """
    response = modelRoomGen.generate_content(prompt)
    character_data = json.loads(response.text)

    return Character(
        name=character_data["name"],
        age=character_data["age"],
        gender=character_data["gender"],
        level=character_data["level"],
        hp=character_data["hp"],
        alignment=character_data["alignment"],
        description=character_data["description"],
        background=character_data["background"],
        wealth=character_data["wealth"],
        strength=character_data["strength"],
        dexterity=character_data["dexterity"],
        constitution=character_data["constitution"],
        wisdom=character_data["wisdom"],
        intelligence=character_data["intelligence"],
        charisma=character_data["charisma"],
        classs=character_data["class"]
    )
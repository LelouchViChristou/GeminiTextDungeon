# room_generation.py
import json
import random

def generate_room(x: int, y: int, model):
    room_types = [
        "standard_room",
        "puzzle_room",
        "quest_room",
        "event_room",
        "treasure_room",
        "boss_room"
    ]
    room_type = random.choice(room_types)
    
    prompt = f"""
    Generate a detailed description for a {room_type.replace('_', ' ')} at coordinates ({x}, {y}) in a fantasy RPG game.
    Include atmospheric details, potential interactions, and any special features.
    
    Using this JSON schema:
      Room = {{
        "room_name": str,
        "description": str,
        "items": list[str],
        "creatures": list[str],
        "exits": list[str],
        "room_type": str,
        "special_feature": str
      }}
    
    For puzzle rooms, include a riddle or puzzle in the special_feature.
    For quest rooms, include a quest description in the special_feature.
    For event rooms, describe a random event in the special_feature.
    For treasure rooms, list valuable items in the items field.
    For boss rooms, include a formidable enemy in the creatures field and describe it in the special_feature.
    
    Return a single `Room` object.
    """
    
    response = model.generate_content(prompt)
    room_data = json.loads(response.text)
    return room_data

def print_room_details(room):
    print(f"Room Name: {room['room_name']}")
    print(f"Room Type: {room['room_type'].replace('_', ' ').title()}")
    print(f"Description: {room['description']}")
    print("Items in the room:")
    for item in room['items']:
        print(f"  - {item}")
    print("Creatures in the room:")
    for creature in room['creatures']:
        print(f"  - {creature}")
    print("Available exits:")
    for exit in room['exits']:
        print(f"  - {exit}")
    if room['special_feature']:
        print(f"Special Feature: {room['special_feature']}")
    print("-" * 40)  # Separator for readability
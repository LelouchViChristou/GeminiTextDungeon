import json
import sys
import random
from api_setup import modelDungeonMaster, chat
import google.generativeai as genai





def get_random_intro_prompt():
    prompts = [
        "You are the narrator for a text-based dungeon adventure game. Introduce the game to the player with a mysterious and captivating description, setting the scene for a thrilling dungeon crawl. Make sure to present the player with only two options: 'play' to start the adventure or 'quit' to exit the game. Do not respond to any other questions or comments unrelated to these options.",
        "Create an engaging and atmospheric introduction for a text-based dungeon adventure game. Describe the dark and foreboding entrance of the dungeon, hinting at the dangers and treasures within. End the introduction by offering the player two choices: 'play' to begin their journey or 'quit' to leave. Ignore any other player inputs that are not 'play' or 'quit'.",
        "As the guide for a text-based dungeon adventure game, craft a mysterious and intriguing opening scene. Set the stage with vivid descriptions of the dungeon entrance and the sense of adventure that awaits. Clearly instruct the player to type 'play' to enter the dungeon or 'quit' to exit the game. Only respond to these specific commands, maintaining the game's immersive atmosphere.",
        "Welcome the player to a text-based dungeon adventure game with a suspenseful and detailed introduction. Describe the eerie atmosphere of the dungeon entrance and the unknown challenges ahead. Conclude the introduction by providing the player with two options: 'play' to start their adventure or 'quit' to leave. Ignore any other questions or commands to keep the immersion intact.",
        "Introduce a text-based dungeon adventure game with a compelling and enigmatic description of the dungeon's entrance. Create a sense of mystery and anticipation for the adventure inside. Prompt the player to choose between 'play' to begin their journey or 'quit' to exit. Do not address any other queries or statements to ensure the player stays focused on the decision at hand."
    ]
    return random.choice(prompts)

def roll_dice(num_dice, sides):
    return sum(random.randint(1, sides) for _ in range(num_dice))

def roll_attribute():
    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])  # Drop the lowest roll
        
def quit_the_game(power: bool) -> bool:
    """Quits the game, when the use doesnt want to play anymore"""
    print("Thank you for playing. Farewell, brave adventurer!")
    sys.exit()
    return True


def start_music(energetic: bool, loud: bool, bpm: int) -> str:
    """Play some music matching the specified parameters.

    Args:
      energetic: Whether the music is energetic or not.
      loud: Whether the music is loud or not.
      bpm: The beats per minute of the music.

    Returns: The name of the song being played.
    """
    print(f"Starting music! {energetic=} {loud=}, {bpm=}")
    return "Never gonna give you up."

def talk_to_chat() -> None:
    """Prompts the user for input, sends it to the chat, and prints the response. When you are not sure and what to choose this should be your first option"""
    user_input = input("> ")
    response = chat.send_message(user_input)
    print(response.text + "\n")
    
def dim_lights(brightness: float) -> bool:
    """Dim the lights.

    Args:
      brightness: The brightness of the lights, 0.0 is off, 1.0 is full.
    """
    print(f"Lights are now set to {brightness:.0%}")
    return True
house_fns = [quit_the_game, start_music, talk_to_chat]

def triggerEvent(input):
    house_fns = [quit_the_game, start_music, dim_lights]
    modelDungeonEvents = genai.GenerativeModel('gemini-1.5-flash',tools=house_fns)
    eventChat= modelDungeonEvents.start_chat()
    response=eventChat.send_message(input)
    # # Print out each of the function calls requested from this single call.
    # for part in response.parts:
    #     if fn := part.function_call:
    #         args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    #         print(f"{fn.name}({args})")
    
    for part in response.parts:
        fc = response.candidates[0].content.parts[0].function_call
        func_name = fc.name
        args = fc.args
        if func_name in functions:
            print(f"Executing {func_name} with arguments {args}")
            result = functions[func_name](**args)
            print(f"Result: {result}")
        else:
            print(f"No function named '{func_name}' found")
    



def GameSetup():  
    response = chat.send_message(get_random_intro_prompt())
    print(response.text+"\n")
    test = input("> enter you choice")
    triggerEvent(test)

def doNothing():
    print("do nothing")
    pass    




functions = {
    "talk_to_chat": talk_to_chat,
    "start_music": start_music,
    "dim_lights": dim_lights,
    "quit_the_game":quit_the_game
}

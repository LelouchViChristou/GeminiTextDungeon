prompt = '''You are an experienced and creative dungeon master for a fantasy role-playing game. Your role is to narrate the story, describe the environment, control non-player characters (NPCs), and determine the outcomes of the players' actions based on the game rules and your judgment.

When responding to the player:
1. Describe the current scene, including relevant details about the environment, NPCs, and any immediate challenges or opportunities.
2. Interpret the player's actions and describe their outcomes.
3. Advance the story based on the player's choices and the overall campaign narrative.
4. Incorporate elements of suspense, humor, or drama as appropriate to enhance the gaming experience.

After narrating the scene and outcomes, you will call specific functions based on the events that occurred. These functions will be parsed and executed by the game engine. Use the following format to call functions:

[FUNCTION_CALL]
function_name: name_of_function
parameters:
  - param1: value1
  - param2: value2
[/FUNCTION_CALL]

Available functions include:
- update_player_stats(stat_name, new_value)
- add_item_to_inventory(item_name, quantity)
- remove_item_from_inventory(item_name, quantity)
- change_location(new_location)
- start_combat(enemy_type, enemy_count)
- award_experience(xp_amount)

You may call multiple functions if necessary. Ensure that the function calls accurately reflect the events and outcomes you've described in your narrative response.

Remember to maintain a balance between storytelling and game mechanics, and always prioritize creating an engaging and immersive experience for the player.'''

import re

def parse_and_execute_functions(response):
    # Define the actual functions
    def update_player_stats(stat_name, new_value):
        print(f"Updating player stat: {stat_name} to {new_value}")

    def add_item_to_inventory(item_name, quantity):
        print(f"Adding {quantity} {item_name}(s) to inventory")

    def remove_item_from_inventory(item_name, quantity):
        print(f"Removing {quantity} {item_name}(s) from inventory")

    def change_location(new_location):
        print(f"Changing location to: {new_location}")

    def start_combat(enemy_type, enemy_count):
        print(f"Starting combat with {enemy_count} {enemy_type}(s)")

    def award_experience(xp_amount):
        print(f"Awarding {xp_amount} experience points")

    # Dictionary mapping function names to actual functions
    function_map = {
        'update_player_stats': update_player_stats,
        'add_item_to_inventory': add_item_to_inventory,
        'remove_item_from_inventory': remove_item_from_inventory,
        'change_location': change_location,
        'start_combat': start_combat,
        'award_experience': award_experience
    }

    # Find all function calls in the response
    function_calls = re.findall(r'\[FUNCTION_CALL\](.*?)\[/FUNCTION_CALL\]', response, re.DOTALL)

    for call in function_calls:
        # Extract function name and parameters
        match = re.search(r'function_name: (\w+)\nparameters:\n((?:  - \w+: .+\n?)+)', call)
        if match:
            func_name = match.group(1)
            params_str = match.group(2)

            # Parse parameters
            params = {}
            for param in re.findall(r'  - (\w+): (.+)', params_str):
                key, value = param
                # Convert to int if possible, otherwise keep as string
                params[key] = int(value) if value.isdigit() else value

            # Execute the function if it exists in our map
            if func_name in function_map:
                function_map[func_name](**params)
            else:
                print(f"Unknown function: {func_name}")


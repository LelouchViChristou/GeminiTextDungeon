# main.py
from character import Character, generate_character
from game_mechanics import GameSetup
from room_generation import print_room_details
from grid import Grid
from room_generation import print_room_details
from api_setup import modelRoomGen

# Main game loop
def main():
#     print("""
# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                        LEGENDS OF THE FORGOTTEN REALMS                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# Hark, brave soul! You stand at the threshold of destiny, poised to etch your 
# name into the annals of history. The mists of time part before you, revealing 
# a world of magic, peril, and untold adventure.

# But first, we must know of the hero who dares to challenge fate. Speak now, 
# and let your words shape the very essence of your being!

# Tell us your name, weave the tapestry of your past, and whisper the legend 
# you aspire to become. From the depths of your imagination, a hero shall rise!

# ✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧

# Scribe your tale below, O Stalwart Adventurer:
# (Include your name, a brief backstory, and the legend you wish to forge)

# """)
#     new_character = generate_character()
#     print(new_character.get_status())
#     GameSetup()
    grid = Grid(10, 10)
    player_x, player_y = 5, 5

    for _ in range(4):
            current_tile = grid.get_tile(player_x, player_y)
            if not current_tile.discovered:
                room_data = grid.generate_tile_data(player_x, player_y, modelRoomGen)
                print(f"\nYou have discovered a new area at ({player_x}, {player_y})!")
                print_room_details(room_data)
                
                # Handle special room types
                if room_data['room_type'] == 'puzzle_room':
                    print("Solve the puzzle to proceed!")
                    # Add puzzle-solving logic here
                elif room_data['room_type'] == 'quest_room':
                    print("A new quest is available!")
                    # Add quest acceptance logic here
                elif room_data['room_type'] == 'event_room':
                    print("An event is unfolding!")
                    # Add event resolution logic here
                elif room_data['room_type'] == 'boss_room':
                    print("Prepare for a challenging battle!")
                    # Add boss battle logic here
            else:
                print(f"\nYou are at a familiar location: ({player_x}, {player_y})")
                print_room_details(current_tile.data)

            # Get player input
            action = input("\nWhat would you like to do? ").lower().strip()

            if action in ['north', 'south', 'east', 'west']:
                new_x, new_y = grid.move_player(player_x, player_y, action)
                if (new_x, new_y) != (player_x, player_y):
                    player_x, player_y = new_x, new_y
                    print(f"You move {action}.")
                else:
                    print("You can't move in that direction.")
            elif action == 'interact':
                # Implement room interaction logic
                print("You interact with the room...")
                if current_tile.data['room_type'] == 'puzzle_room':
                    # Implement puzzle solving
                    puzzle_answer = input("Enter your answer to the puzzle: ")
                    # Check if the answer is correct
                    # Reward the player if correct
                elif current_tile.data['room_type'] == 'quest_room':
                    # Implement quest acceptance
                    accept_quest = input("Do you want to accept the quest? (yes/no): ").lower()
                    if accept_quest == 'yes':
                        print("Quest accepted!")
                        # Add quest to player's quest log
                elif current_tile.data['room_type'] == 'event_room':
                    # Implement event resolution
                    print("You engage with the event...")
                    # Resolve the event and apply consequences
                elif current_tile.data['room_type'] == 'boss_room':
                    # Implement boss battle
                    print("You engage in battle with the boss!")
                    # Implement turn-based combat system
                elif current_tile.data['room_type'] == 'treasure_room':
                    # Implement treasure collection
                    print("You search the room for treasure...")
                    # Add items to player's inventory
            elif action == 'inventory':
                # Display player's inventory
                print("Your inventory:")
                # Implement inventory display logic
            elif action == 'quit':
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid action. Please try again.")
if __name__ == "__main__":
    main()
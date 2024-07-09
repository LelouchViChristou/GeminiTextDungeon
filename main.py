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


        
    for _ in range(4):
        current_tile = grid.get_tile(grid.player_x, grid.player_y)
        if not current_tile.discovered:
            room_data = grid.generate_tile_data(grid.player_x, grid.player_y, modelRoomGen)
            print(f"\nYou have discovered a new area at ({grid.player_x}, {grid.player_y})!")
            print_room_details(room_data)

        else:
            print(f"\nYou are at a familiar location: ({grid.player_x}, {grid.player_y})")
            print_room_details(current_tile.data)

        # Get player input
        action = input("\nWhat would you like to do? (north/south/east/west/quit) ").lower().strip()

        if action in ['north', 'south', 'east', 'west']:
            moved = grid.move_player(action)
            if moved:
                print(f"You move {action}.")
            else:
                print(f"You can't move {action} from here.")
        elif action == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid action. Please choose 'north', 'south', 'east', 'west', or 'quit'.")


           
if __name__ == "__main__":
    main()
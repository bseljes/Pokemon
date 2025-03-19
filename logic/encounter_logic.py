import random
from movement import generate_random_key
from pokemon_spawns import spawn_info
import encounter_maps
def get_encounter_areas():
    # instance_area = {}
    # with open('G:/My Drive/python/Pokemon Yellow/logic/encounter_areas.py', 'r') as file:
    #     lines = file.readlines()
    #     # Remove leading/trailing whitespace from each line
    #     lines = [line.strip() for line in lines]
        
    #     # Group lines into pairs of tuples
    #     for i in range(0, len(lines), 2):
    #         tuple1 = eval(lines[i])  # Convert string to tuple
    #         tuple2 = eval(lines[i+1])  # Convert string to tuple
    #         grouped_tuples = (tuple1, tuple2)

    #         # Create a dictionary with random keys
    #         key = generate_random_key(instance_area)
    #         instance_area[key] = grouped_tuples

    # encounter_dict = {
    #     'Route 1': instance_area
    # }

    # with open('G:/My Drive/python/Pokemon Yellow/logic/encounter_maps.py', 'w') as outFile:
    #     outFile.write(f'encounter_grass = {encounter_dict}\n')
    encounter_dict = encounter_maps.encounter_grass
    return encounter_dict


def is_encounter(map_x, map_y):
    spawns = get_encounter_areas()
    for area in spawns:
        for coordinate in spawns[area]:
            x1 = spawns[area][coordinate][0][0]
            y1 = spawns[area][coordinate][0][1]
            x2 = spawns[area][coordinate][1][0]
            y2 = spawns[area][coordinate][1][1]
            if map_x >= min(x1, x2) and map_x <= max(x1, x2) and map_y <= max(y1, y2) and map_y >= min(y1, y2):
                true_or_false = list(range(1, 15))
                encounter = random.choices(true_or_false)
                if encounter == [1]:
                    return True
                else:
                    return False

def choose_pokemon(route):
    pokemon_spawn = spawn_info[route]['land']
    pokemon_list = pokemon_spawn[0]
    spawn_ratios = pokemon_spawn[1]
    spawn_levels = pokemon_spawn[2]
    # Randomly select a Pokemon based on the spawn ratios
    pokemon = random.choices(pokemon_list, weights=spawn_ratios)[0]
    level = random.choice(spawn_levels)
    return level, pokemon

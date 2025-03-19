import string
import random
import collision_values
PLAYERSTEP = 50

surfing = False

def get_collisions():
    instance_collisions = {}
    with open('collisions.py', 'r') as file:
        lines = file.readlines()
        # Remove leading/trailing whitespace from each line
        lines = [line.strip() for line in lines]
        
        # Group lines into pairs of tuples
        for i in range(0, len(lines), 2):
            tuple1 = eval(lines[i])  # Convert string to tuple
            tuple2 = eval(lines[i+1])  # Convert string to tuple
            grouped_tuples = (tuple1, tuple2)
    
    # Create a dictionary with random keys
            key = generate_random_key(instance_collisions)
            instance_collisions[key] = grouped_tuples
        return instance_collisions
    
def get_water():
    instance_water = {}
    with open('water.py', 'r') as file:
        lines = file.readlines()
        # Remove leading/trailing whitespace from each line
        lines = [line.strip() for line in lines]
        
        # Group lines into pairs of tuples
        for i in range(0, len(lines), 2):
            tuple1 = eval(lines[i])  # Convert string to tuple
            tuple2 = eval(lines[i+1])  # Convert string to tuple
            grouped_tuples = (tuple1, tuple2)
    
    # Create a dictionary with random keys
            key = generate_random_key(dict=instance_water)
            instance_water[key] = grouped_tuples
        return instance_water

def generate_random_key(dict, length=8):
    letters = string.ascii_lowercase
    while letters in dict.keys():
        letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def add_collisions_key_value(key):
    collisions = collision_values.collision_info['collisions']
    # collisions[key] = get_collisions()  # Used to add new points to collisions
    water = collision_values.collision_info['water']
    # water[key] = get_water()   # Used to add new points to water
    exceptions = collision_values.collision_info['exceptions']
    # exceptions[key] = get_collision_exceptions()  # Used to add new points to exceptions
    ledges = collision_values.collision_info['ledges']
    # ledges[key] = get_ledges('up')   # Used to add new point to ledges
    collision_info = {'collisions': collisions,
                      'water': water,
                      'exceptions': exceptions,
                      'ledges': ledges
    }

    with open('collision_values.py', 'w') as outFile:
        outFile.write(f'collision_info = {collision_info}\n')

    return collisions, water, exceptions, ledges

def get_collision_exceptions():
    instance_exceptions = {}
    with open('logic/collide_excpetions.py', 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Assuming each line contains a tuple in the format "(x, y)"
            line = line.strip()
            if line.startswith("(") and line.endswith(")"):
                try:
                    # Convert the line to a tuple
                    tuple_data = eval(line)
                    # Generate a random key for the dictionary
                    key = generate_random_key(instance_exceptions)
                    # Add the tuple to the dictionary using the generated key
                    instance_exceptions[key] = tuple_data
                except SyntaxError:
                    # Ignore lines that don't contain valid tuples
                    continue
    return instance_exceptions

def get_ledges(stop):
    # Get tuples of tuples to add to to collisions info
    instance_ledges = {}
    with open('ledgeup.py', 'r') as file:
        lines = file.readlines()
        # Remove leading/trailing whitespace from each line
        lines = [line.strip() for line in lines]
        
        # Group lines by two
        for i in range(0, len(lines), 2):
            tuple1 = eval(lines[i])  # Convert strings to tuple
            tuple2 = eval(lines[i+1])
            grouped_tuples = (tuple1, tuple2)
    
    # Create instance dictionary with random keys
            key = generate_random_key(instance_ledges)
            instance_ledges[key] = {
                'instance': grouped_tuples,
                'stop': stop
            }
    return instance_ledges

def collision(map_x, map_y, dir):
    collisions, water, exceptions, ledges = add_collisions_key_value('pallet_town')
    clear = True
    for map in collisions:
        for key in collisions[map]:
            x1 = collisions[map][key][0][0]
            y1 = collisions[map][key][0][1]
            x2 = collisions[map][key][1][0]
            y2 = collisions[map][key][1][1]
            # going up counts up
            if map_x <= max(x1, x2) and map_x >= min(x1, x2) and map_y + PLAYERSTEP >= min(y1, y2) and map_y + PLAYERSTEP <= max(y2, y1) and dir == 'Up':
                if (map_x, map_y + PLAYERSTEP) not in exceptions.values():
                    clear = False
            # going down counts down
            elif map_x <= max(x1, x2) and map_x >= min(x1, x2) and map_y - PLAYERSTEP >= min(y1, y2) and map_y - PLAYERSTEP <= max(y1, y2) and dir == 'Down':
                if (map_x, map_y - PLAYERSTEP) not in exceptions.values():
                    clear = False
            # going right counts down
            elif map_y <= max(y1, y2) and map_y >= min(y1, y2) and map_x - PLAYERSTEP <= max(x1, x2) and map_x - PLAYERSTEP >= min(x2, x1) and dir == 'Right':
                if (map_x - PLAYERSTEP, map_y)  not in exceptions.values():
                    clear = False
            # going left counts up
            elif map_y <= max(y1, y2) and map_y >= min(y1, y2) and map_x + PLAYERSTEP <= max(x1, x2) and map_x + PLAYERSTEP >= min(x1, x2) and dir == 'Left':
                if (map_x + PLAYERSTEP, map_y) not in exceptions.values():
                    clear = False

    for map in water:
        for key in water[map]:
            x1 = water[map][key][0][0]
            y1 = water[map][key][0][1]
            x2 = water[map][key][1][0]
            y2 = water[map][key][1][1]
            # going up counts up
            if map_x <= max(x1, x2) and map_x >= min(x1, x2) and map_y + PLAYERSTEP >= min(y1, y2) and map_y + PLAYERSTEP <= max(y2, y1) and dir == 'Up':
                if surfing == False:
                    clear = False
            # going down counts down
            elif map_x <= max(x1, x2) and map_x >= min(x1, x2) and map_y - PLAYERSTEP >= min(y1, y2) and map_y - PLAYERSTEP <= max(y1, y2) and dir == 'Down':
                if surfing == False:
                    clear = False
            # going right counts down
            elif map_y <= max(y1, y2) and map_y >= min(y1, y2) and map_x - PLAYERSTEP <= max(x1, x2) and map_x - PLAYERSTEP >= min(x2, x1) and dir == 'Right':
                if surfing == False:
                    clear = False
            # going left counts up
            elif map_y <= max(y1, y2) and map_y >= min(y1, y2) and map_x + PLAYERSTEP <= max(x1, x2) and map_x + PLAYERSTEP >= min(x1, x2) and dir == 'Left':
                if surfing == False:
                    clear = False
    for map in ledges:
        for key in ledges[map]:
            x1 = ledges[map][key]['instance'][0][0]
            y1 = ledges[map][key]['instance'][0][1]
            x2 = ledges[map][key]['instance'][1][0]
            y2 = ledges[map][key]['instance'][1][1]
            stop = ledges[map][key]['stop']
            if stop == 'up':
                if map_x <= max(x1, x2) and map_x >= min(x1, x2) and map_y + PLAYERSTEP == y1 and dir == 'Up':
                    clear = False
                elif map_x <= max(x1, x2) and map_x >= min(x1, x2) and map_y - PLAYERSTEP == y1 and dir == 'Down':
                    clear = False
            elif stop == 'left':
                if map_y <= max(y1, y2) and map_x >= min(y1, y2) and map_x + PLAYERSTEP == x1 and dir == 'left':
                    clear = False
            elif stop == 'right':
                if map_y <= max(y1, y2) and map_y >= min(y1, y2) and map_x - PLAYERSTEP == x1 and dir == 'Right':
                    clear = False
    return clear


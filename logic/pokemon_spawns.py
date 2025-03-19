import random

spawn_info = {
    'Route 1': {
        'land': [
            ['Pidgey', 'Rattata'],
            [0.55, 0.45],
            [2, 3, 4, 5, 6]
        ],
        'water': []
    },
    'Route 2': {
        'land': [
            ['Pidgey', 'Rattata', 'Caterpie', 'Weedle'],
            [0.39, 0.39, 0.1, 0.1]
        ],
        'water': []
    },
    'Route 3': {
        'land': [
            ['Pidgey', 'Rattata', 'Spearow', 'Sandshrew', 'Jigglypuff', 'Mankey'],
            [0.39, 0.39, 0.1, 0.1, 0.01, 0.01]
        ],
        'water': []
    },
    'Route 4': {
        'land': [
            ['Rattata', 'Spearow', 'Ekans', 'Sandshrew'],
            [0.55, 0.45, 0.01, 0.01]
        ],
        'water': []
    },
    'Route 5': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Meowth', 'Mankey'],
            [0.35, 0.05, 0.39, 0.1, 0.1]
        ],
        'water': []
    },
    'Route 6': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Meowth', 'Mankey'],
            [0.35, 0.05, 0.39, 0.1, 0.1]
        ],
        'water': []
    },
    'Route 7': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Meowth', 'Mankey'],
            [0.35, 0.05, 0.39, 0.1, 0.1]
        ],
        'water': []
    },
    'Route 8': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Meowth', 'Mankey'],
            [0.35, 0.05, 0.39, 0.1, 0.1]
        ],
        'water': []
    },
    'Route 9': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Spearow', 'Ekans', 'Sandshrew'],
            [0.35, 0.05, 0.35, 0.1, 0.1, 0.05]
        ],
        'water': []
    },
    'Route 10': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Spearow', 'Ekans', 'Sandshrew'],
            [0.35, 0.05, 0.35, 0.1, 0.1, 0.05]
        ],
        'water': []
    },
    'Route 11': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Spearow', 'Ekans', 'Sandshrew', 'Drowzee'],
            [0.35, 0.05, 0.35, 0.1, 0.1, 0.05, 0.05]
        ],
        'water': []
    },
    'Route 12': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell'],
            [0.35, 0.05, 0.2, 0.05, 0.2, 0.1, 0.05]
        ],
        'water': []
    },
    'Route 13': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell'],
            [0.35, 0.05, 0.2, 0.05, 0.2, 0.1, 0.05]
        ],
        'water': []
    },
    'Route 14': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell'],
            [0.35, 0.05, 0.2, 0.05, 0.2, 0.1, 0.05]
        ],
        'water': []
    },
    'Route 15': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Oddish', 'Gloom', 'Venonat', 'Bellsprout', 'Weepinbell'],
            [0.35, 0.05, 0.2, 0.05, 0.2, 0.1, 0.05]
        ],
        'water': []
    },
    'Route 16': {
        'land': [
            ['Rattata', 'Raticate', 'Spearow'],
            [0.4, 0.05, 0.55]
        ],
        'water': []
    },
    'Route 17': {
        'land': [
            ['Rattata', 'Raticate', 'Spearow'],
            [0.4, 0.05, 0.55]
        ],
        'water': []
    },
    'Route 18': {
        'land': [
            ['Rattata', 'Raticate', 'Spearow'],
            [0.4, 0.05, 0.55]
        ],
        'water': []
    },
    'Route 19': {
        'land': [
            ['Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok'],
            [0.35, 0.05, 0.15, 0.05, 0.15, 0.05]
        ],
        'water': [
            ['Tentacool'],
            [0.8]
        ]
    },
    'Route 20': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Raticate', 'Spearow', 'Fearow'],
            [0.35, 0.05, 0.35, 0.05, 0.15, 0.05]
        ],
        'water': []
    },
    'Route 21': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Raticate', 'Tangela'],
            [0.35, 0.05, 0.35, 0.05, 0.2]
        ],
        'water': []
    },
    'Route 22': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Spearow', 'Nidoran (female)', 'Nidoran (male)'],
            [0.4, 0.05, 0.4, 0.05, 0.05, 0.05]
        ],
        'water': []
    },
    'Route 23': {
        'land': [
            ['Pidgey', 'Pidgeotto', 'Rattata', 'Raticate', 'Spearow', 'Fearow'],
            [0.35, 0.05, 0.35, 0.05, 0.15, 0.05]
        ],
        'water': []
    },
    'Route 24': {
        'land': [
            ['Caterpie', 'Metapod', 'Weedle', 'Kakuna', 'Pidgey', 'Pidgeotto', 'Oddish', 'Gloom'],
            [0.15, 0.1, 0.15, 0.1, 0.35, 0.05, 0.1, 0.1]
        ],
        'water': []
    },
    'Route 25': {
        'land': [
            ['Caterpie', 'Metapod', 'Weedle', 'Kakuna', 'Pidgey', 'Pidgeotto', 'Oddish', 'Gloom'],
            [0.15, 0.1, 0.15, 0.1, 0.35, 0.05, 0.1, 0.1]
        ],
        'water': []
    },
    'Diglett\'s Cave': {
        'land': [
            ['Diglett'],
            [1.0]
        ],
        'water': []
    },
    'Pokémon Tower': {
        'land': [
            ['Gastly', 'Cubone'],
            [0.8, 0.2]
        ],
        'water': []
    },
    'Seafoam Islands': {
        'land': [],
        'water': [
            ['Tentacool', 'Shellder'],
            [0.8, 0.2]
        ]
    },
    'Seafoam Islands B1F': {
        'land': [
            ['Zubat', 'Golbat'],
            [0.8, 0.2]
        ],
        'water': [
            ['Tentacool', 'Shellder'],
            [0.8, 0.2]
        ]
    },
    'Seafoam Islands B2F': {
        'land': [
            ['Zubat', 'Golbat'],
            [0.8, 0.2]
        ],
        'water': [
            ['Tentacool', 'Shellder'],
            [0.8, 0.2]
        ]
    },
    'Seafoam Islands B3F': {
        'land': [
            ['Zubat', 'Golbat'],
            [0.8, 0.2]
        ],
        'water': [
            ['Tentacool', 'Shellder'],
            [0.8, 0.2]
        ]
    },
    'Victory Road 1F': {
        'land': [
            ['Zubat', 'Machop', 'Geodude', 'Graveler', 'Onix'],
            [0.35, 0.35, 0.2, 0.05, 0.05]
        ],
        'water': []
    },
    'Victory Road 2F': {
        'land': [
            ['Zubat', 'Machop', 'Geodude', 'Graveler', 'Onix'],
            [0.35, 0.35, 0.2, 0.05, 0.05]
        ],
        'water': []
    },
    'Victory Road 3F': {
        'land': [
            ['Zubat', 'Machop', 'Geodude', 'Graveler', 'Onix'],
            [0.35, 0.35, 0.2, 0.05, 0.05]
        ],
        'water': []
    },
    'Viridian Forest': {
        'land': [
            ['Caterpie', 'Metapod', 'Weedle', 'Kakuna', 'Pidgey', 'Pidgeotto'],
            [0.2, 0.1, 0.2, 0.1, 0.3, 0.1]
        ],
        'water': []
    },
    'Diglett\'s Cave': {
        'land': [
            ['Diglett', 'Dugtrio'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Indigo Plateau': {
        'land': [
            ['Rattata', 'Raticate', 'Spearow', 'Fearow', 'Jynx', 'Ditto'],
            [0.25, 0.1, 0.1, 0.05, 0.05, 0.05]
        ],
        'water': []
    },
    'Safari Zone': {
        'land': [
            ['Nidoran (male)', 'Nidorina', 'Nidorino', 'Paras', 'Venonat', 'Exeggcute', 'Rhyhorn', 'Chansey', 'Kangaskhan', 'Scyther', 'Pinsir', 'Tauros'],
            [0.1, 0.05, 0.05, 0.2, 0.1, 0.1, 0.05, 0.05, 0.05, 0.04, 0.04, 0.17]
        ],
        'water': []
    },
    'Power Plant': {
        'land': [
            ['Pikachu', 'Magnemite', 'Magneton', 'Grimer', 'Voltorb', 'Electrode', 'Electabuzz'],
            [0.1, 0.3, 0.05, 0.2, 0.25, 0.05, 0.05]
        ],
        'water': []
    },
    'Pewter City Gym': {
        'land': [
            ['Geodude', 'Onix'],
            [0.8, 0.2]
        ],
        'water': []
    },
    'Cerulean City Gym': {
        'land': [
            ['Staryu', 'Starmie'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Vermilion City Gym': {
        'land': [
            ['Voltorb', 'Electrode'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Celadon City Gym': {
        'land': [
            ['Weepinbell', 'Victreebel'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Fuchsia City Gym': {
        'land': [
            ['Venonat', 'Venomoth'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Saffron City Gym': {
        'land': [
            ['Kadabra', 'Mr. Mime'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Cinnabar Island Gym': {
        'land': [
            ['Growlithe', 'Arcanine'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Viridian City Gym': {
        'land': [
            ['Gym Leader Giovanni'],
            [1.0]
        ],
        'water': []
    },
    'Pokemon Mansion': {
        'land': [
            ['Rattata', 'Raticate', 'Grimer', 'Muk', 'Koffing', 'Weezing'],
            [0.3, 0.1, 0.2, 0.05, 0.2, 0.15]
        ],
        'water': []
    },
    'Cerulean Cape': {
        'land': [
            ['Pidgey', 'Rattata'],
            [0.5, 0.5]
        ],
        'water': [
            ['Tentacool'],
            [1.0]
        ]
    },
    'Celadon Mansion': {
        'land': [
            ['Gastly', 'Haunter'],
            [0.9, 0.1]
        ],
        'water': []
    },
    'Cinnabar Island': {
        'land': [
            ['Growlithe', 'Arcanine', 'Ponyta', 'Rapidash', 'Magmar'],
            [0.3, 0.1, 0.3, 0.1, 0.2]
        ],
        'water': []
    }
}



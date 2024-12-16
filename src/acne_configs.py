# CONSTANT

ACNE_ID = {
    'hyperpigmented_papules_(dark_spots)': 0,
    'inflammatory_lesions_(papules,_pustules,_erythematous_plaques)': 1,
    'acne_scars_(depressed,_convex)': 2,
    'pustules_(closed/open)': 3,
    'cystic_and_nodular_lesions': 4
}

ID_SHORTDESC = {
    0: 'dark_spots',
    1: 'inflammatory_lesions',
    2: 'acne_scars',
    3: 'pustules',
    4: 'cystic_lesions'
}

ID_COLOR = {
    0: (25, 25, 180), # strong-blue/blue-black
    1: (255, 128, 255), # pink
    2: (0, 155, 0), # green
    3: (100, 230, 230), # light blue
    4: (230, 0, 0) # red
}

# Float
ID_COLOR_FLOAT = {
    0: (0.1, 0.1, 0.7), # strong-blue/blue-black
    1: (1.0, 0.5, 1.0), # pink
    2: (0, 0.6, 0), # green
    3: (0.4, 0.9, 0.9), # light blue
    4: (0.9, 0, 0), # red
}
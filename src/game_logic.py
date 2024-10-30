import random

# Define the minimum size of the rooms
MIN_ROOM_SIZE = 10

# Define the size of the dungeon (room) and its objects
def generate_fixed_room(room_number):
    # Predefined rooms with sizes and object placements
    rooms = {
        1: {"width": 8, "height": 8, "objects": {(2, 2): "Chest", (5, 5): "Torch Stand"}},
        2: {"width": 9, "height": 9, "objects": {(1, 1): "Cracked Wall", (7, 7): "Locked Door"}},
        3: {"width": 10, "height": 10, "objects": {(3, 3): "Chest", (6, 6): "Torch Stand"}},
        4: {"width": 8, "height": 8, "objects": {(4, 4): "Locked Door"}},
        5: {"width": 8, "height": 8, "objects": {(4, 4): "Chest"}},  # Special room with Echo Lens upgrade
        6: {"width": 12, "height": 12, "objects": {(3, 3): "Torch Stand", (8, 8): "Cracked Wall"}},
        7: {"width": 10, "height": 10, "objects": {(2, 2): "Chest", (5, 5): "Locked Door"}},
        8: {"width": 12, "height": 12, "objects": {(6, 6): "Cracked Wall", (10, 10): "Torch Stand"}},
        9: {"width": 9, "height": 9, "objects": {(1, 1): "Chest", (8, 8): "Locked Door"}},
        10: {"width": 11, "height": 11, "objects": {(5, 5): "Torch Stand", (7, 7): "Cracked Wall"}},
    }
    
    # Return the selected room layout based on room number
    room = rooms.get(room_number, {"width": 10, "height": 10, "objects": {}})
    return {"width": room["width"], "height": room["height"], "objects": room["objects"]}


# Initial room size dictionary
    room_size = {"width": width, "height": height}

# Dictionary to store room objects with their positions
    room_objects = {}

# Use a set to track used positions for objects
    used_positions = set()


 # Place a door on one of the walls (left, right, top, or bottom wall)
    wall_side = random.choice(["left", "right", "top", "bottom"])
    if wall_side == "left":
        door_position = (0, random.randint(1, height - 2))  # Left wall, avoid corners
    elif wall_side == "right":
        door_position = (width - 1, random.randint(1, height - 2))  # Right wall
    elif wall_side == "top":
        door_position = (random.randint(1, width - 2), 0)  # Top wall
    else:
        door_position = (random.randint(1, width - 2), height - 1)  # Bottom wall

    room_objects[door_position] = "Locked Door"
    used_positions.add(door_position)  # Mark door position as used

    # Define the types of objects to be placed in various rooms
    object_types = ["Chest", "Torch Stand", "Cracked Wall"]

    # Randomly determine the number of objects to place (between 3 and 6 for variety)
    num_objects = random.randint(3, 6)

    # Place each object randomly within room boundaries, ensuring unique positions
    for _ in range(num_objects):
        obj_type = random.choice(object_types)

        # Generate unique position within room boundaries, avoiding the door location
        while True:
            x = random.randint(1, width - 2)  # Avoid wall edges for regular objects
            y = random.randint(1, height - 2)
            position = (x, y)
            if position not in used_positions:  # Ensure no overlap
                used_positions.add(position)
                room_objects[position] = obj_type
                break

    return room_size, room_objects
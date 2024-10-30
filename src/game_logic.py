# Define the size and objects of each fixed room
def generate_fixed_room(room_number):
    # Predefined rooms with sizes and object placements
    rooms = {
        1: {"width": 8, "height": 8, "objects": {(2, 2): "Chest", (5, 5): "Torch Stand"}},
        2: {"width": 9, "height": 9, "objects": {(1, 1): "Cracked Wall", (7, 7): "Locked Door"}},
        3: {"width": 10, "height": 10, "objects": {(3, 3): "Chest", (6, 6): "Torch Stand"}},
        4: {"width": 8, "height": 8, "objects": {(4, 4): "Locked Door"}},
        5: {"width": 8, "height": 8, "objects": {(4, 4): "Chest"}},  # Room 5 with Echo Lens upgrade
        6: {"width": 12, "height": 12, "objects": {(3, 3): "Torch Stand", (8, 8): "Cracked Wall"}},
        7: {"width": 10, "height": 10, "objects": {(2, 2): "Chest", (5, 5): "Locked Door"}},
        8: {"width": 12, "height": 12, "objects": {(6, 6): "Cracked Wall", (10, 10): "Torch Stand"}},
        9: {"width": 9, "height": 9, "objects": {(1, 1): "Chest", (8, 8): "Locked Door"}},
        10: {"width": 11, "height": 11, "objects": {(5, 5): "Torch Stand", (7, 7): "Cracked Wall"}},
    }
    
    # Return the selected room layout based on room number
    room = rooms.get(room_number, {"width": 10, "height": 10, "objects": {}})
    return {"width": room["width"], "height": room["height"], "objects": room["objects"]}

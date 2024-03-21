"""Object oriented adventure game.

Code written mostly by GitHub Copilot. Superwised by Rikard."""

class Room:
    """Room class for the game."""
    def __init__(self, name, description):
        """Call constructor to create a room."""
        self.name = name
        self.description = description
        self.linked_rooms = {}

    def link_room(self, room_to_link, direction):
        """Link a room to another room."""
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        """String representation of the room."""
        print(self.name)
        print("----------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.name + " is " + direction)

    def move(self, direction):
        """Move to a linked room.
        
        direction: str, the direction to move.
        For example "north", "south", "east", "west".
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
        
class House:
    """House class for the game."""
    def __init__(self):
        """Call constructor to create a house."""
        self.rooms = {}

    def add_room(self, room):
        """Add a room to the house."""
        self.rooms[room.name] = room

    def get_room(self, room_name):
        """Get a room from the house."""
        return self.rooms[room_name]

    def get_room_details(self, room_name):
        """Get details of a room from the house."""
        return self.rooms[room_name].get_details()

class Game:
    """Game class for the adventure game."""
    def __init__(self):
        """Call constructor to create a adventure game."""
        self.house = House()
        self.current_room = None

    def create_rooms(self):
        """Create rooms for the game."""
        living_room = Room("Living Room", "A large room with a TV")
        kitchen = Room("Kitchen", "A small room with a sink")
        dining_room = Room("Dining Room", "A medium room with a table")
        living_room.link_room(kitchen, "east")
        kitchen.link_room(dining_room, "south")
        dining_room.link_room(living_room, "west")
        self.house.add_room(living_room)
        self.house.add_room(kitchen)
        self.house.add_room(dining_room)
        self.current_room = living_room

    def play(self):
        """Play the game.
        
        Call to start the game.
        """
        print("Welcome to the game")
        print("Type 'quit' to exit")
        while True:
            self.current_room.get_details()
            command = input("> ")
            if command == "quit":
                break
            self.current_room = self.current_room.move(command)

game = Game()
game.create_rooms()
game.play()
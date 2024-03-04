class Room:
    def __init__(self, description, north, east, south, west, up, down):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down

def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    print("Welcome to your new mansion have a look around.")

    # Entry Hall - 0
    room = Room("\nYou are in the entry hall. \nYou can go north, west, or up the stairs.", 3, None, None, 1, 2, None)
    room_list.append(room)

    # Living Room - 1
    room = Room("\nYou are in the living room. \nYou can exit to the east.", None, 0, None, None, None, None)
    room_list.append(room)

    # Stairs - 2
    room = Room("\nYou are at the stairs on the second floor. \nYou can either go to the north or back downstairs.", 14, None, None, None, None, 0)
    room_list.append(room)

    # Main Hall - 3
    room = Room("\nYou are in the main hall. \nYou can go to the north, east, or west.", 9, 4, 0, 10, None, None)
    room_list.append(room)

    # Dining Room - 4
    room = Room("\nYou are in the dining room. \nYou can go the the east or west.", None, 5, None, 3, None, None)
    room_list.append(room)

    # Kitchen - 5
    room = Room("\nYou are in the kitchen. \nYou can go to the east or west.", None, 6, None, 4,None,None)
    room_list.append(room)

    # east Hall - 6
    room = Room("\nYou are in the east hall. \nYou can go to the north, south, or west.", 7, None, 8, 5,None,None)
    room_list.append(room)

    # Bedroom 1 - 7
    room = Room("\nYou are in bedroom one. \nYou can exit to the south.", None, None, 6, None,None, None)
    room_list.append(room)

    # Gym - 8
    room = Room("\nYou are in the gym. \nYou can exit to the north.", 6, None, None, None, None, None)
    room_list.append(room)

    # Ball Room - 9
    room = Room("\nYou are in the ball room. \nYou can exit to the south.", None, None, 3,None, None, None)
    room_list.append(room)

    # West Hall - 10
    room = Room("\nYou are in the west hall. \nYou can go to the north, east, or south.", 13, 3, 11, None, None, None)
    room_list.append(room)

    # Library 1st Floor - 11
    room = Room("\nYou are in the library. \nYou can exit to the north or go up the stairs.", 10, None, None, 1, 12, None)
    room_list.append(room)

    # Library 2nd Floor - 12
    room = Room("\nYou are on the second floor library. \nYou can go back downstairs or exit to the east.", None,14, None, None, None, 11)
    room_list.append(room)

    # Bedroom 2 -13
    room = Room("\nYou are in the second bedroom. \nYou can exit to the south.", None, None, 10, None, None, None)
    room_list.append(room)

    # 2nd Floor Hall - 14
    room = Room("\nYou are in the second floor hall. \nYou can go to the north, east, south, or west.", 15, 16, 2, 12, None, None)
    room_list.append(room)

    # Study - 15
    room = Room("\nYou are now in the study. \nYou can exit to the south.", None, None,14,None, None, None)
    room_list.append(room)

    # Bedroom 3 - 16
    room = Room("\nYou are in the third bedroom. \n You can exit to the west.", None, None, None, 14, None, None)
    room_list.append(room)

    while not done:
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n e s w u d)").lower()
        if direction[0] =='n': # North
            next_room = room_list[current_room].north

        elif direction[0] =='s': # South
            next_room = room_list[current_room].south

        elif direction[0] =='e': # East
            next_room = room_list[current_room].east

        elif direction[0] =='w': # West
            next_room = room_list[current_room].west

        elif direction[0] == 'u': # Up
            next_room = room_list[current_room].up

        elif direction[0] == 'd': # Down
            next_room = room_list[current_room].down

        elif direction[0] =='q': # Quit
            done = True

        else:
            print("Please pick a valid direction.")
            continue

        if next_room == None:
            print("You cannot go that way!")
            continue

        current_room = next_room

main()
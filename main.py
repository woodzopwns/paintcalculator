from house import Paint, Wall, Room, House


def user_input(is_string):
    retrieve_input = None
    valid = False
    while not valid:
        try:
            if is_string:
                retrieve_input = str(input())
                valid = True
            else:
                retrieve_input = float(input())
                valid = True
        except ValueError:
            print(f'''Sorry! That's not the answer I was expecting!\n''')
    return retrieve_input


# Introduction
print('Hello! Welcome to the house paint price calculator\n'
      'this calculator will show you the price of painting your house\n'
      'internal or external :).\n')

# Take user input on number of rooms
print('How many rooms will be in your house?')
number_rooms = user_input(False)

# Take user input on paint details
print('How much does your paint cost per can?')
paint_cost = user_input(False)
print('How many metres does your paint cover per can?')
paint_coverage = user_input(False)

# Making a list of rooms to be added to the house later
rooms = []
for room in range(int(number_rooms)):
    rooms.append(Room())

# I don't know what the fuck this is
for itx, room in enumerate(rooms):
    print(f'How many walls are in room {itx + 1}?')
    number_walls = int(input())

    for wall in range(number_walls):
        print(f'How wide is wall {wall + 1}?')
        width = user_input(False)
        print(f'How tall is wall {wall + 1}?')
        height = user_input(False)
        new_wall = Wall(width, height)
        print(f'Are there any obstructions on wall {wall + 1}? [Y/N]')

        if user_input(True).upper() == "Y":
            print(f'Is it circular or square? [C/S]')
            obstruction_type = user_input(True).upper()
            if obstruction_type == "S":
                print(f'What is the obstruction height?')
                obstruction_height = user_input(False)
                print(f'And the width?')
                obstruction_width = user_input(False)
                new_wall.add_square_obstruction(height, width)
            elif obstruction_type == "C":
                print(f'What is the obstruction radius?')
                obstruction_radius = user_input(False)
                new_wall.add_circular_obstruction(obstruction_radius)
        else:
            rooms[itx].add_wall(new_wall)

# Adding the rooms with their newly added walls to the house
house = House()
for room in rooms:
    house.add_room(room)

# Placeholder paint stuffs
blue_paint = Paint(10, 10)
price = blue_paint.calculate_price(house.get_house_area())

# Final price to 2 decimals as per currency standards
print(f'Your final price is: £%.2f' % price)

# ___________________________ TO DO (in order) ___________________________
# User input validation as a function (take str or int)
# Paint type input functionality
# Full input functionality
# Unit testing
# E2E testing
# Comment code more comprehensively
# Saving data into CSV file
# Consider adding a user interface functionality

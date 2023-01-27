from house import Paint, Wall, Room, House


# Function to take user input, with input checks and error handling
def user_input(is_string):
    retrieve_input = None
    is_valid = False
    while not is_valid:
        try:
            if is_string:
                retrieve_input = str(input())
                is_valid = True
            else:
                retrieve_input = float(input())
                is_valid = True
        except ValueError:
            print(f'''Sorry! That's not the answer I was expecting!\n''')
    return retrieve_input


# Tuple with default paints
paint_types = (Paint(25, 25), Paint(27, 20), Paint(26, 22), Paint(18, 24),
               Paint(17, 25), Paint(19, 20), Paint(10, 25.5), Paint(10, 25.5))

# Introduction
print('Hello! Welcome to the house paint price calculator\n'
      'this calculator will show you the price of painting your house\n'
      'internal or external :).\n')

# Take user input on number of rooms
print('How many rooms will be in your house?')
number_rooms = user_input(False)

# Take user input on paint details
print('Would you like to use your own paint? If not you can select from '
      'our custom set [Y/N]')
custom_paint = user_input(True).upper()

# Loop inputs to get correct responses
valid = False
while not valid:
    # Take paint properties if they want to use their own
    if custom_paint == "Y":
        print('How much does your paint cost per can?')
        paint_cost = user_input(False)
        print('How many metres does your paint cover per can?')
        paint_coverage = user_input(False)
        paint = Paint(paint_cost, paint_coverage)
        valid = True
    # If they don't want to use custom paint
    elif custom_paint == "N":
        # List paint types
        print('Please select from the following options:')
        print('1. Dulux White Paint (£25 can, 25m coverage')
        print('2. Dulux Beige Paint (£27 can, 20m coverage')
        print('3. Dulux Brown Paint (£26 can, 22m coverage')
        print('4. Albany Yellow Paint (£18 can, 24m coverage')
        print('5. Albany Baby Milk Paint (£17 can, 25m coverage')
        print('6. Albany Pale Ghost Paint (£19 can, 20m coverage')
        print('7. Budget White Paint (£10 can, 25.5m coverage')
        print('8. Budget Beige Paint (£10 can, 25.5m coverage')
        # Checking that the number is between 1 and 8
        num_check = False
        while not num_check:
            try:
                paint_type = user_input(False)
                if paint_type > 8 or paint_type < 1:
                    raise ValueError('Number less than 0 or more than 8')
                num_check = True
            except ValueError:
                print('Sorry, please enter a number between 0 and 8')
        # Setting the paint type
        paint = paint_types[int(paint_type-1)]
        valid = True
    # Re-loop as it wasn't a correct response
    else:
        print('''Sorry, that wasn't a correct answer''')

# Making a list of rooms to be added to the house later
rooms = []
for room in range(int(number_rooms)):
    rooms.append(Room())

# For every room in rooms take number of walls
for itx, room in enumerate(rooms):
    print(f'How many walls are in room {itx + 1}?')
    number_walls = int(input())

    # For every wall take width and height and instantiate a new wall
    for wall in range(number_walls):
        print(f'How wide is wall {wall + 1}?')
        width = user_input(False)
        print(f'How tall is wall {wall + 1}?')
        height = user_input(False)
        new_wall = Wall(width, height)
        print(f'Are there any obstructions on wall {wall + 1}? [Y/N]')

        # If there is an obstruction
        if user_input(True).upper() == "Y":
            print(f'Is it circular or square? [C/S]')
            obstruction_type = user_input(True).upper()
            # If obstruction is square
            if obstruction_type == "S":
                print(f'What is the obstruction height?')
                obstruction_height = user_input(False)
                print(f'And the width?')
                obstruction_width = user_input(False)
                new_wall.add_square_obstruction(height, width)
            # If obstruction is circular
            elif obstruction_type == "C":
                print(f'What is the obstruction radius?')
                obstruction_radius = user_input(False)
                new_wall.add_circular_obstruction(obstruction_radius)

        # Add the wall to the room
        rooms[itx].add_wall(new_wall)

# Adding the rooms with their newly added walls to the house
house = House()
for room in rooms:
    house.add_room(room)

# Get final price
price = paint.calculate_price(house.get_house_area())

# Final price to 2 decimals as per currency standards
print(f'Your final price is: £%.2f' % price)

# ___________________________ TO DO (in order) ___________________________
# Unit testing
# E2E testing
# Saving data into CSV file
# Consider adding a user interface functionality

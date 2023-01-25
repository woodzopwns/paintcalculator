from House import Paint, Wall, Room, House

# Introduction
print('Hello! Welcome to the house paint price calculator\n'
      'this calculator will show you the price of painting your house\n'
      'internal or external :).\n')

# Take user input on number of rooms
valid = False
while not valid:
    try:
        print('How many rooms will be in your house?')
        number_rooms = int(input())
        valid = True
    except ValueError:
        print('Sorry! I need a number!\n')

# Take user input on paint details
valid = False
while not valid:
    try:
        print('How much does your paint cost per can?')
        paint_cost = int(input())
        print('How many metres does your paint cover per can?')
        paint_coverage = int(input())
        valid = True
    except ValueError:
        print('Sorry! I need a number!\n')

rooms = []
for room in range(number_rooms):
    rooms.append(Room())

for itx, room in enumerate(rooms):
    print(f'How many walls are in room {itx+1}?')
    number_walls = int(input())
    for wall in range(number_walls):
        print(f'How wide is wall {wall}?')
        width = int(input())
        print(f'How tall is wall {wall}?')
        height = int(input())
        new_wall = Wall(width, height)
        print(f'Are there any obstructions on wall {wall+1}? [Y/N]')
        if str(input()).upper() == "Y":
            print(f'Is it circular or square? [C/S]')
            obstruction_type = str(input())
            if obstruction_type.upper() == "S":
                print(f'What is the obstruction height?')
                obstruction_height = int(input())
                print(f'And the width?')
                obstruction_width = int(input())
                new_wall.add_square_obstruction(height, width)
            elif obstruction_type.upper() == "C":
                print(f'What is the obstruction radius?')
                obstruction_radius = int(input())
                new_wall.add_circular_obstruction(obstruction_radius)
        else:
            rooms[itx].add_wall(new_wall)

house = House()
for room in rooms:
    house.add_room(room)

blue_paint = Paint(10, 10)
price = blue_paint.calculate_price(house.get_house_area())

print(f'Your final price is: £{price}')

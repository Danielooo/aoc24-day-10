grid = None
current_pos = [0, 0]
amount_found_trails = 0

current_pos_trail_pos = None
current_pos_trail_altitude = 0
current_pos_junction = None
current_junction_left_over_directions = []


def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    grid = [[int(char) if char.isdigit() else char for char in line.strip()] for line in lines]
    return grid


def print_grid(grid):
    for row in grid:
        print(row)


def is_possible_start_trail(char):
    if char == 0:
        return True
    else:
        return False


def find_trail_from_start_pos(y, x):
    current_altitude = 0
    check_left()


def check_up():
    global current_pos_trail_pos
    global current_pos_trail_altitude
    y, x = current_pos_trail_pos
    print(grid[y - 1][x])
    if y > 0 and grid[y - 1][x] != '.':
        if grid[y - 1][x] == current_pos_trail_altitude + 1:
            current_pos_trail_pos = [y - 1, x]
            current_pos_trail_altitude += 1


def check_right():
    global current_pos_trail_pos
    global current_pos_trail_altitude
    y, x = current_pos_trail_pos
    if x < len(grid[y]) - 1 and grid[y][x + 1] != '.':
        if grid[y][x + 1] == current_pos_trail_altitude + 1:
            current_pos_trail_pos = [y, x + 1]
            current_pos_trail_altitude += 1


def check_down():
    global current_pos_trail_pos
    global current_pos_trail_altitude
    y, x = current_pos_trail_pos
    if y < len(grid) - 1 and grid[y + 1][x] != '.':
        if grid[y + 1][x] == current_pos_trail_altitude + 1:
            current_pos_trail_pos = [y + 1, x]
            current_pos_trail_altitude += 1


def check_left():
    global current_pos_trail_pos
    global current_pos_trail_altitude
    y, x = current_pos_trail_pos
    if x > 0 and grid[y][x - 1] != '.':
        if grid[y][x - 1] == current_pos_trail_altitude + 1:
            current_pos_trail_pos = [y, x - 1]
            current_pos_trail_altitude += 1


def is_junction_test():
    amount_of_directions = 0
    next_altitude = current_pos_trail_altitude + 1
    # UP
    if y > 0 and grid[y - 1][x] == next_altitude:
        amount_of_directions += 1
    # RIGHT
    if x < len(grid[0]) - 1 and grid[y][x + 1] == next_altitude:
        amount_of_directions += 1

    # DOWN
    if y < len(grid) - 1 and grid[y + 1][x] == next_altitude:
        amount_of_directions += 1

    # LEFT
    if x > 0 and grid[y][x - 1] == next_altitude:
        amount_of_directions += 1

    if amount_of_directions > 1:
        print(amount_of_directions)
        print(current_pos_trail_pos)



def is_junction():
    global current_pos_junction
    global current_junction_left_over_directions
    next_altitude = current_pos_trail_altitude + 1
    y, x = current_pos_trail_pos
    # UP
    if y > 0 and grid[y - 1][x] == next_altitude:
        current_junction_left_over_directions.append('^')
    # RIGHT
    if x < len(grid[0]) - 1 and grid[y][x + 1] == next_altitude:
        current_junction_left_over_directions.append('>')
    # DOWN
    if y < len(grid) - 1 and grid[y + 1][x] == next_altitude:
        current_junction_left_over_directions.append('v')
    # LEFT
    if x > 0 and grid[y][x - 1] == next_altitude:
        current_junction_left_over_directions.append('<')

    print(current_pos_trail_pos)
    print(current_junction_left_over_directions)
    current_junction_left_over_directions = []

    if len(current_junction_left_over_directions) > 1:
        current_pos_junction = [y, x]
        print(current_pos_junction)
        print(current_junction_left_over_directions)
    else:
        current_junction_left_over_directions = []



def print_pos():
    print('found trail')
    print(current_pos_trail_pos)
    print(current_pos_trail_altitude)


if __name__ == '__main__':
    grid = read_file_to_grid("test.txt")
    print_grid(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                print("found zero", y, x)
                print(0)
                current_pos = [y, x]
                current_pos_trail_pos = [y, x]
                while(True):
                    is_junction_test()
                    check_up()

                    check_right()

                    check_down()

                    check_left()

                    if current_pos_trail_altitude == 9:
                        amount_found_trails += 1
                        current_pos_trail_altitude = 0
                        break

    print('amount found trails: ', amount_found_trails)

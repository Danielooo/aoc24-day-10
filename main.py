grid = None
current_pos = [0, 0]
amount_found_trails = 0

current_pos_trail_pos = None
current_pos_trail_altitude = 0


def read_file_to_grid(filename):
    with open (filename, 'r') as file:
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
    if y <= 0 and grid[y][x + 1] != '.':
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
                print(0)
                current_pos = [y, x]
                current_pos_trail_pos = [y, x]
                while(True):
                    check_up()
                    check_right()
                    check_down()
                    check_left()
                    if current_pos_trail_altitude == 9:
                        amount_found_trails += 1
                        break

    print('amount found trails: ', amount_found_trails)





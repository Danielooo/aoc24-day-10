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


def check_left():
    y, x = current_pos
    if grid[y][x - 1] != '.':
        if grid[y][x - 1] == current_pos_trail_altitude + 1:
            print('found trail')


if __name__ == '__main__':
    grid = read_file_to_grid("test.txt")
    print_grid(grid)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                current_pos = [y, x]
                print()
                print(current_pos)
                check_left()



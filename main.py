def read_file_to_grid(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [[int(char) if char.isdigit() else char for char in line.strip()] for line in lines]


def print_grid(grid):
    for row in grid:
        print(row)


def is_possible_start_trail(char):
    return char == 1


def check_direction(grid, current_pos, current_altitude, direction):
    y, x = current_pos
    if direction == 'up' and y > 0 and grid[y - 1][x] == current_altitude + 1:
        return [y - 1, x]
    elif direction == 'right' and x < len(grid[y]) - 1 and grid[y][x + 1] == current_altitude + 1:
        return [y, x + 1]
    elif direction == 'down' and y < len(grid) - 1 and grid[y + 1][x] == current_altitude + 1:
        return [y + 1, x]
    elif direction == 'left' and x > 0 and grid[y][x - 1] == current_altitude + 1:
        return [y, x - 1]
    return None


def find_junction(grid, current_pos, current_altitude):
    y, x = current_pos
    next_altitude = current_altitude + 1
    directions = []

    if y > 0 and grid[y - 1][x] == next_altitude:
        directions.append('up')
    if x < len(grid[0]) - 1 and grid[y][x + 1] == next_altitude:
        directions.append('right')
    if y < len(grid) - 1 and grid[y + 1][x] == next_altitude:
        directions.append('down')
    if x > 0 and grid[y][x - 1] == next_altitude:
        directions.append('left')

    return directions if len(directions) > 1 else None


def find_all_trails(grid, start_pos, max_length=5):
    stack = [(start_pos, 1, [start_pos])]
    all_trails = []

    while stack:
        current_pos, current_altitude, trail = stack.pop()
        y, x = current_pos

        if len(trail) == max_length:
            all_trails.append(trail)
            continue

        for direction in ['up', 'right', 'down', 'left']:
            new_pos = check_direction(grid, current_pos, current_altitude, direction)
            if new_pos and new_pos not in trail:
                stack.append((new_pos, current_altitude + 1, trail + [new_pos]))

    return all_trails


def find_trails(grid):
    all_trails = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_possible_start_trail(grid[y][x]):
                current_pos = [y, x]
                all_trails.extend(find_all_trails(grid, current_pos))

    return all_trails, len(all_trails)


if __name__ == '__main__':
    grid = read_file_to_grid('small.txt')
    print_grid(grid)
    all_trails, trail_count = find_trails(grid)
    print('Number of trails found: ', trail_count)
    for trail in all_trails:
        print(' -> '.join(map(str, trail)))
        print('---')
from collections import defaultdict

def is_symbol(c):
    return not c.isdigit() and c != '.'

def within_bounds(row, col, world):
    width = len(world[0])
    height = len(world)

    return row < width and row >= 0 and col >= 0 and col < height

def eligible_digit(row, col, world, visited):
    return within_bounds(row, col, world) and not visited[(row, col)] and world[row][col].isdigit()

def search_west(row, col, world, visited=defaultdict(bool)):
    num = ""
    j = col - 1
    while eligible_digit(row, j, world, visited):
        num = world[row][j] + num
        visited[(row, j)] = True
        j -= 1
    return num

def search_east(row, col, world, visited=defaultdict(bool)):
    num = ""
    j = col + 1
    while eligible_digit(row, j, world, visited):
        num += world[row][j]
        visited[(row, j)] = True
        j += 1
    return num

def search(row, col, world, visited):
    adjacent_part_score = 0
    
    # NW, N, NE
    if eligible_digit(row - 1, col, world, visited):
        adjacent_part_score += int(search_west(row - 1, col, world, visited) + world[row - 1][col] + search_east(row - 1, col, world, visited))
    else:
        part_w = search_west(row - 1, col, world, visited)
        adjacent_part_score += int(part_w) if part_w else 0

        part_e = search_east(row - 1, col, world, visited)
        adjacent_part_score += int(part_e) if part_e else 0

    # W
    part = search_west(row, col, world, visited)
    adjacent_part_score += int(part) if part else 0

    # SW, S, SE
    if eligible_digit(row + 1, col, world, visited):
        adjacent_part_score += int(search_west(row + 1, col, world, visited) + world[row + 1][col] + search_east(row + 1, col, world, visited))
    else:
        part_w = search_west(row + 1, col, world, visited)
        adjacent_part_score += int(part_w) if part_w else 0

        part_e = search_east(row + 1, col, world, visited)
        adjacent_part_score += int(part_e) if part_e else 0

    # E
    part = search_east(row, col, world, visited)
    adjacent_part_score += int(part) if part else 0

    return adjacent_part_score

def search_gears(row, col, world):
    adjacent_parts = []
    # NW, N, NE
    if within_bounds(row - 1, col, world) and world[row - 1][col].isdigit():
        adjacent_parts.append(int(search_west(row - 1, col, world) + world[row - 1][col] + search_east(row - 1, col, world)))
    else:
        part_w = search_west(row - 1, col, world)
        if part_w:
            adjacent_parts.append(int(part_w))

        part_e = search_east(row - 1, col, world)
        if part_e:
            adjacent_parts.append(int(part_e))

    # W
    part = search_west(row, col, world)
    if part:
        adjacent_parts.append(int(part))

    # SW, S, SE
    if within_bounds(row + 1, col, world) and world[row + 1][col].isdigit():
        adjacent_parts.append(int(search_west(row + 1, col, world) + world[row + 1][col] + search_east(row + 1, col, world)))
    else:
        part_w = search_west(row + 1, col, world)
        if part_w:
            adjacent_parts.append(int(part_w))

        part_e = search_east(row + 1, col, world)
        if part_e:
            adjacent_parts.append(int(part_e))

    # E
    part = search_east(row, col, world)
    if part:
        adjacent_parts.append(int(part))

    return adjacent_parts[0] * adjacent_parts[1] if len(adjacent_parts) == 2 else 0

def solve_a():
    visited = defaultdict(bool)

    part_sum = 0
    world = []

    # Construct grid
    while line := input():
        temp = []
        for c in line:
            temp.append(c)
        world.append(temp)

    width = len(world[0])
    height = len(world)
    for row in range(height):
        for col in range(width):
            if is_symbol(world[row][col]):
                part_sum += search(row, col, world, visited)
            
    return part_sum

def solve_b():
    gear_sum = 0
    world = []

    # Construct grid
    while line := input():
        temp = []
        for c in line:
            temp.append(c)
        world.append(temp)

    width = len(world[0])
    height = len(world)
    for row in range(height):
        for col in range(width):
            if world[row][col] == '*':
                gear_sum += search_gears(row, col, world)
            
    return gear_sum
